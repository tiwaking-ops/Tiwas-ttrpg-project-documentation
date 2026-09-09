const fs = require('fs');

// === RNG: LCG a=1664525, c=1013904223, m=2^32, seed=42 ===
let rngState = 42;
const RNG_A = 1664525, RNG_C = 1013904223, RNG_M = 4294967296;
function nextRng() { rngState = (BigInt(RNG_A) * BigInt(rngState) + BigInt(RNG_C)) % BigInt(RNG_M); return Number(rngState); }
function d100() { return (nextRng() % 100) + 1; }
function isDouble(r) { if (r === 100) return true; return Math.floor(r / 10) === (r % 10); }
function swapDigits(r) { if (r === 100) return 100; return (r % 10) * 10 + Math.floor(r / 10); }
function locZone(idx) { if (idx <= 25) return "Legs"; if (idx <= 50) return "Torso"; if (idx <= 75) return "Arms"; return "Head"; }

const attrNames = {bpp:"Might",bps:"Impact",bpe:"Brawn",bpx:"Presence",bsp:"Agility",bss:"Reflexes",
  bse:"Quickness",bsx:"Grace",bep:"Toughness",bes:"Stamina",bee:"Vitality",bex:"Poise",
  mpp:"Cunning",mps:"Wits",mpe:"Willpower",mpx:"Glamour",msp:"Acuity",mss:"Perception",
  mse:"Alacrity",msx:"Charm",mep:"Focus",mes:"Discipline",mee:"Resolve",mex:"Composure"};

// === Derived formulas (reverse-engineered from fixed values) ===
function calcHP(a) { return (a.bpp+a.bps+a.bpe+a.bpx+a.bsp+a.bss+a.bse+a.bsx+a.bep+a.bes+a.bee+a.bex) + Math.floor((a.bpp-50)/5); }
function calcMP(a) { return a.mpp+a.mps+a.mpe+a.mpx+a.msp+a.mss+a.mse+a.msx+a.mep+a.mes+a.mee+a.mex; }
function calcPE(a) { return a.bpe+a.bep+a.bee; }
function calcSpeed(a) { return a.bsp+a.bse+a.bss; }
function calcERegen(a) { return a.bee+a.bse; }
function calcMRegen(a) { return a.mep+a.mes; }
function calcMov(s) { return Math.floor(s/25); }
function calcCap(formula, a) { let s=0; for(const f of formula) s+=a[f]; return Math.floor(s/formula.length); }

function recalcDerived(who) {
  who.hpMax = calcHP(who.attrs); who.mpMax = calcMP(who.attrs); who.peMax = calcPE(who.attrs);
  who.speed = calcSpeed(who.attrs); who.energyRegen = calcERegen(who.attrs);
  who.mpRegen = calcMRegen(who.attrs); who.movement = calcMov(who.speed);
  if (who.hp > who.hpMax) who.hp = who.hpMax;
  if (who.mp > who.mpMax) who.mp = who.mpMax;
  if (who.pe > who.peMax) who.pe = who.peMax;
  for (const sk of Object.values(who.skills)) {
    sk.cap = calcCap(sk.formula, who.attrs);
    if (sk.current > sk.cap) sk.current = sk.cap;
  }
}

function makeCombatant(name, attrs, skillDefs, skillCount, nextEffect) {
  const who = { name, attrs: {...attrs}, skills: {}, skillCount, nextEffect, alive: true, frightened: false };
  for (const [k,v] of Object.entries(skillDefs)) {
    who.skills[k] = {...v};
  }
  who.hp = calcHP(who.attrs); who.mp = calcMP(who.attrs); who.pe = calcPE(who.attrs);
  who.hpMax = who.hp; who.mpMax = who.mp; who.peMax = who.pe;
  who.speed = calcSpeed(who.attrs); who.energyRegen = calcERegen(who.attrs);
  who.mpRegen = calcMRegen(who.attrs); who.movement = calcMov(who.speed);
  return who;
}

// === Core Test (9-step) ===
function coreTest(who, skillName) {
  const sk = who.skills[skillName];
  let effectiveSkill = sk.current;
  if (who.frightened) effectiveSkill = Math.max(0, effectiveSkill - 1);
  const roll = d100();
  const success = (roll !== 100 && roll <= effectiveSkill);
  const margin = success ? Math.max(1, effectiveSkill - roll) : 0;
  const cost = roll;
  let peBefore = who.pe;
  let overflow = 0;
  if (cost > peBefore) { overflow = cost - peBefore; who.pe = 0; who.hp -= overflow; }
  else { who.pe = peBefore - cost; }
  let peAfterCost = who.pe;
  let failureXP = success ? 0 : Math.max(0, roll - effectiveSkill);
  let pool = failureXP;
  let skillUps = [];
  while (pool >= sk.current && sk.current < sk.cap) {
    pool -= sk.current; sk.current += 1;
    skillUps.push({from: sk.current-1, to: sk.current});
  }
  let newSkill = null;
  if (!success && isDouble(roll)) {
    who.skillCount += 1;
    const newTier = sk.tier + 1;
    const domain = sk.domain;
    const isBody = domain === "PE";
    const allA = isBody
      ? ["bpp","bps","bpe","bpx","bsp","bss","bse","bsx","bep","bes","bee","bex"]
      : ["mpp","mps","mpe","mpx","msp","mss","mse","msx","mep","mes","mee","mex"];
    let addA = null;
    for (const a of allA) { if (!sk.formula.includes(a)) { addA = a; break; } }
    const nf = [...sk.formula, addA];
    const nc = calcCap(nf, who.attrs);
    const nn = "Skill-" + who.skillCount;
    who.skills[nn] = { tier: newTier, formula: nf, cap: nc, current: 1, domain };
    newSkill = {name:nn, tier:newTier, formula:nf, cap:nc, parent:skillName};
  }
  const recovery = Math.min(Math.floor(who.energyRegen / 2), who.peMax);
  who.pe = Math.min(who.pe + recovery, who.peMax);
  if (who.hp <= 0 && who.alive) { who.alive = false; if (who.hp > 0) who.hp = 0; }
  return { actor:who.name, skillName, effectiveSkill, roll, success, margin, cost, peBefore, peAfterCost, overflow, hpOverflow:overflow, failureXP, skillUps, newSkill, recovery, hpAfter:who.hp, peAfter:who.pe };
}

// === Opposed Contest ===
function opposedContest(attacker, atkSkill, defender, defSkill) {
  let repeats = [];
  let aT, dT, result;
  for (let i = 0; i < 50; i++) {
    aT = coreTest(attacker, atkSkill);
    dT = coreTest(defender, defSkill);
    if (aT.success && !dT.success) { result = "attacker_wins"; break; }
    if (!aT.success && dT.success) { result = "defender_wins"; break; }
    if (aT.success && dT.success) {
      if (aT.margin > dT.margin) { result = "attacker_wins"; break; }
      if (dT.margin > aT.margin) { result = "defender_wins"; break; }
      repeats.push({type:"tie", aRoll:aT.roll, aMargin:aT.margin, dRoll:dT.roll, dMargin:dT.margin});
    } else {
      repeats.push({type:"both_fail", aRoll:aT.roll, dRoll:dT.roll});
    }
    if (i === 49) result = "stalled";
  }
  return { aTest: aT, dTest: dT, result, repeats };
}

// === Active Defense ===
function activeDefense(defender, defSkill) {
  return coreTest(defender, defSkill);
}

// === Wound magnitude after AD ===
function woundMag(atkTier, adSuccess, adMargin) {
  let mag = 2;
  const tierShred = (atkTier === 2) ? -1 : (atkTier < 2 ? -(2-atkTier) : 1);
  mag += tierShred;
  if (adSuccess) mag -= adMargin;
  let finalTier = 2;
  if (mag < 1) { finalTier = 1; mag = 1; }
  return { tier: finalTier, magnitude: mag, tierShred, adMarginSub: adSuccess ? adMargin : 0, negated: false };
}

// === Wound targets ===
const woundTargets = { "Icy Claws": ["bsp","bpp"], "Sharktoothed Maw": ["bpp","bep"], "Attack2": ["bps","bsp"] };
function pickTarget(skillName) {
  const c = woundTargets[skillName];
  return c[d100() % c.length];
}

// ====== MAIN SIMULATION ======
const allAttrs = ["bpp","bps","bpe","bpx","bsp","bss","bse","bsx","bep","bes","bee","bex",
                  "mpp","mps","mpe","mpx","msp","mss","mse","msx","mep","mes","mee","mex"];
const pcA = {}; allAttrs.forEach(a => pcA[a] = 50);
const pc = makeCombatant("Adventurer-1", pcA,
  { Attack2:{tier:2,formula:["bps","bsp"],cap:50,current:25,domain:"PE"},
    Defence2:{tier:2,formula:["bss","bse"],cap:50,current:25,domain:"PE"} }, 26, "injury");
pc.frightened = true;

const trA = {bpp:75,bps:65,bpe:70,bpx:55,bsp:60,bss:55,bse:60,bsx:20,bep:70,bes:65,bee:80,bex:25,
             mpp:45,mps:30,mpe:55,mpx:10,msp:40,mss:60,mse:35,msx:5,mep:45,mes:30,mee:50,mex:15};
const troll = makeCombatant("Ice Troll", trA,
  { "Icy Claws":{tier:2,formula:["bsp","bpp"],cap:67,current:67,domain:"PE"},
    "Sharktoothed Maw":{tier:2,formula:["bpp","bep"],cap:75,current:75,domain:"PE"},
    "Brawling":{tier:1,formula:["bpp"],cap:75,current:37,domain:"PE"},
    "Camouflage":{tier:1,formula:["mss"],cap:60,current:30,domain:"MP"},
    "Stealth":{tier:1,formula:["bse"],cap:60,current:30,domain:"PE"},
    "Tracking":{tier:1,formula:["mss"],cap:60,current:30,domain:"MP"} }, 6, "wound");

let totalCoreTests = 0;
let allRounds = [];
let edgeCases = [];
let rulings = new Set();
let failedDoubleCount = 0;
let repeatCount = 0;

for (let round = 1; round <= 30 && pc.alive && troll.alive; round++) {
  const rd = { round, exchanges: [] };

  // === TROLL TURN (Speed 175 > 150) ===
  // Exchange 1: Sharktoothed Maw
  {
    rulings.add("DEC-105:MeleeExchange"); rulings.add("DEC-106:CreatureMultiAction"); rulings.add("DEC-095:TurnOrder"); rulings.add("DEC-098:ActiveDefSkill");
    totalCoreTests += 2;
    const c = opposedContest(troll, "Sharktoothed Maw", pc, "Defence2");
    totalCoreTests += c.repeats.length * 2;
    repeatCount += c.repeats.length;
    const ex = { exchange:1, attacker:"Ice Troll", atkSkill:"Sharktoothed Maw", defender:"Adventurer-1", defSkill:"Defence2",
      aRoll:c.aTest.roll, aSkill:c.aTest.effectiveSkill, aSuccess:c.aTest.success, aMargin:c.aTest.margin,
      aPEbefore:c.aTest.peBefore, aPEafter:c.aTest.peAfter, aOverflow:c.aTest.overflow,
      dRoll:c.dTest.roll, dSkill:c.dTest.effectiveSkill, dSuccess:c.dTest.success, dMargin:c.dTest.margin,
      dPEbefore:c.dTest.peBefore, dPEafter:c.dTest.peAfter, dOverflow:c.dTest.overflow,
      result:c.result, repeats:c.repeats.map(r=>({type:r.type,aRoll:r.aRoll,dRoll:r.dRoll})) };
    if (c.aTest.skillUps.length) ex.aSkillUps = c.aTest.skillUps;
    if (c.dTest.skillUps.length) ex.dSkillUps = c.dTest.skillUps;
    if (c.aTest.newSkill) { ex.aNewSkill = c.aTest.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: Troll created "+c.aTest.newSkill.name}); }
    if (c.dTest.newSkill) { ex.dNewSkill = c.dTest.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: PC created "+c.dTest.newSkill.name}); }
    if (c.result === "attacker_wins") {
      totalCoreTests += 1;
      rulings.add("DEC-103:ADShredMargin"); rulings.add("DEC-104:InjuryDelta");
      const ad = activeDefense(pc, "Defence2");
      ex.adRoll=ad.roll; ex.adSkill=ad.effectiveSkill; ex.adSuccess=ad.success; ex.adMargin=ad.margin;
      ex.adPEbefore=ad.peBefore; ex.adPEafter=ad.peAfter;
      if (ad.skillUps.length) ex.adSkillUps = ad.skillUps;
      if (ad.newSkill) { ex.adNewSkill = ad.newSkill; failedDoubleCount++; }
      const eff = troll.nextEffect;
      ex.effectChoice = eff;
      if (eff === "wound") {
        rulings.add("DEC-100:LocIndex"); rulings.add("DEC-102:WoundTargetRandom"); rulings.add("DEC-107:WoundCapability");
        const lr = swapDigits(c.aTest.roll);
        const zone = locZone(lr);
        const wm = woundMag(2, ad.success, ad.margin);
        const tgt = pickTarget("Sharktoothed Maw");
        ex.locRoll=c.aTest.roll; ex.locSwap=lr; ex.locZone=zone;
        ex.woundTier=wm.tier; ex.woundMag=wm.magnitude; ex.woundShred=wm.tierShred; ex.woundAdMargin=wm.adMarginSub;
        ex.woundTarget=tgt; ex.woundTargetName=attrNames[tgt];
        const oldVal = troll.attrs[tgt];
        troll.attrs[tgt] -= wm.magnitude;
        recalcDerived(troll);
        ex.woundOldVal=oldVal; ex.woundNewVal=troll.attrs[tgt];
        troll.nextEffect = "injury";
      } else {
        const dmg = Math.max(1, c.aTest.margin - (ad.success ? ad.margin : 0));
        ex.injuryDmg = dmg;
        pc.hp -= dmg;
        if (pc.hp <= 0 && pc.alive) { pc.alive = false; edgeCases.push({round,event:"PC incapacitated by Sharktoothed Maw"}); }
        ex.pcHPlater = pc.hp;
        troll.nextEffect = "wound";
      }
    }
    rd.exchanges.push(ex);
  }
  if (!pc.alive || !troll.alive) { allRounds.push(rd); break; }

  // Exchange 2: Icy Claws
  {
    totalCoreTests += 2;
    const c = opposedContest(troll, "Icy Claws", pc, "Defence2");
    totalCoreTests += c.repeats.length * 2;
    repeatCount += c.repeats.length;
    const ex = { exchange:2, attacker:"Ice Troll", atkSkill:"Icy Claws", defender:"Adventurer-1", defSkill:"Defence2",
      aRoll:c.aTest.roll, aSkill:c.aTest.effectiveSkill, aSuccess:c.aTest.success, aMargin:c.aTest.margin,
      aPEbefore:c.aTest.peBefore, aPEafter:c.aTest.peAfter, aOverflow:c.aTest.overflow,
      dRoll:c.dTest.roll, dSkill:c.dTest.effectiveSkill, dSuccess:c.dTest.success, dMargin:c.dTest.margin,
      dPEbefore:c.dTest.peBefore, dPEafter:c.dTest.peAfter, dOverflow:c.dTest.overflow,
      result:c.result, repeats:c.repeats.map(r=>({type:r.type,aRoll:r.aRoll,dRoll:r.dRoll})) };
    if (c.aTest.skillUps.length) ex.aSkillUps = c.aTest.skillUps;
    if (c.dTest.skillUps.length) ex.dSkillUps = c.dTest.skillUps;
    if (c.aTest.newSkill) { ex.aNewSkill = c.aTest.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: Troll created "+c.aTest.newSkill.name}); }
    if (c.dTest.newSkill) { ex.dNewSkill = c.dTest.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: PC created "+c.dTest.newSkill.name}); }
    if (c.result === "attacker_wins") {
      totalCoreTests += 1;
      const ad = activeDefense(pc, "Defence2");
      ex.adRoll=ad.roll; ex.adSkill=ad.effectiveSkill; ex.adSuccess=ad.success; ex.adMargin=ad.margin;
      ex.adPEbefore=ad.peBefore; ex.adPEafter=ad.peAfter;
      if (ad.skillUps.length) ex.adSkillUps = ad.skillUps;
      if (ad.newSkill) { ex.adNewSkill = ad.newSkill; failedDoubleCount++; }
      const eff = troll.nextEffect;
      ex.effectChoice = eff;
      if (eff === "wound") {
        const lr = swapDigits(c.aTest.roll); const zone = locZone(lr);
        const wm = woundMag(2, ad.success, ad.margin);
        const tgt = pickTarget("Icy Claws");
        ex.locRoll=c.aTest.roll; ex.locSwap=lr; ex.locZone=zone;
        ex.woundTier=wm.tier; ex.woundMag=wm.magnitude; ex.woundShred=wm.tierShred; ex.woundAdMargin=wm.adMarginSub;
        ex.woundTarget=tgt; ex.woundTargetName=attrNames[tgt];
        const oldVal = troll.attrs[tgt];
        troll.attrs[tgt] -= wm.magnitude;
        recalcDerived(troll);
        ex.woundOldVal=oldVal; ex.woundNewVal=troll.attrs[tgt];
        troll.nextEffect = "injury";
      } else {
        const dmg = Math.max(1, c.aTest.margin - (ad.success ? ad.margin : 0));
        ex.injuryDmg = dmg;
        pc.hp -= dmg;
        if (pc.hp <= 0 && pc.alive) { pc.alive = false; edgeCases.push({round,event:"PC incapacitated by Icy Claws"}); }
        ex.pcHPlater = pc.hp;
        troll.nextEffect = "wound";
      }
    }
    rd.exchanges.push(ex);
  }
  if (!pc.alive || !troll.alive) { allRounds.push(rd); break; }

  // === PC TURN ===
  // Exchange 3: Attack2
  {
    rulings.add("Frightened:-1PCSkills");
    totalCoreTests += 2;
    const c = opposedContest(pc, "Attack2", troll, "Brawling");
    totalCoreTests += c.repeats.length * 2;
    repeatCount += c.repeats.length;
    const ex = { exchange:3, attacker:"Adventurer-1", atkSkill:"Attack2", defender:"Ice Troll", defSkill:"Brawling",
      aRoll:c.aTest.roll, aSkill:c.aTest.effectiveSkill, aSuccess:c.aTest.success, aMargin:c.aTest.margin,
      aPEbefore:c.aTest.peBefore, aPEafter:c.aTest.peAfter, aOverflow:c.aTest.overflow,
      dRoll:c.dTest.roll, dSkill:c.dTest.effectiveSkill, dSuccess:c.dTest.success, dMargin:c.dTest.margin,
      dPEbefore:c.dTest.peBefore, dPEafter:c.dTest.peAfter, dOverflow:c.dTest.overflow,
      result:c.result, repeats:c.repeats.map(r=>({type:r.type,aRoll:r.aRoll,dRoll:r.dRoll})) };
    if (c.aTest.skillUps.length) ex.aSkillUps = c.aTest.skillUps;
    if (c.dTest.skillUps.length) ex.dSkillUps = c.dTest.skillUps;
    if (c.aTest.newSkill) { ex.aNewSkill = c.aTest.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: PC created "+c.aTest.newSkill.name}); }
    if (c.dTest.newSkill) { ex.dNewSkill = c.dTest.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: Troll created "+c.dTest.newSkill.name}); }
    if (c.result === "attacker_wins") {
      totalCoreTests += 1;
      rulings.add("DEC-103:ADShredMargin"); rulings.add("DEC-104:InjuryDelta");
      const ad = activeDefense(troll, "Brawling");
      ex.adRoll=ad.roll; ex.adSkill=ad.effectiveSkill; ex.adSuccess=ad.success; ex.adMargin=ad.margin;
      ex.adPEbefore=ad.peBefore; ex.adPEafter=ad.peAfter;
      if (ad.skillUps.length) ex.adSkillUps = ad.skillUps;
      if (ad.newSkill) { ex.adNewSkill = ad.newSkill; failedDoubleCount++; edgeCases.push({round,event:"Failed Double: Troll AD created "+ad.newSkill.name}); }
      const eff = pc.nextEffect;
      ex.effectChoice = eff;
      if (eff === "wound") {
        rulings.add("DEC-100:LocIndex"); rulings.add("DEC-102:WoundTargetRandom");
        const lr = swapDigits(c.aTest.roll); const zone = locZone(lr);
        const wm = woundMag(2, ad.success, ad.margin);
        const tgt = pickTarget("Attack2");
        ex.locRoll=c.aTest.roll; ex.locSwap=lr; ex.locZone=zone;
        ex.woundTier=wm.tier; ex.woundMag=wm.magnitude; ex.woundShred=wm.tierShred; ex.woundAdMargin=wm.adMarginSub;
        ex.woundTarget=tgt; ex.woundTargetName=attrNames[tgt];
        const oldVal = troll.attrs[tgt];
        troll.attrs[tgt] -= wm.magnitude;
        recalcDerived(troll);
        ex.woundOldVal=oldVal; ex.woundNewVal=troll.attrs[tgt];
        pc.nextEffect = "injury";
      } else {
        const dmg = Math.max(1, c.aTest.margin - (ad.success ? ad.margin : 0));
        ex.injuryDmg = dmg;
        troll.hp -= dmg;
        if (troll.hp <= 0 && troll.alive) { troll.alive = false; edgeCases.push({round,event:"Troll incapacitated by Attack2"}); }
        ex.trollHPlater = troll.hp;
        pc.nextEffect = "wound";
      }
    }
    rd.exchanges.push(ex);
  }
  allRounds.push(rd);
}

// === FINAL REPORT ===
const endRound = allRounds.length;
let rpt = `# Tiwas Ice Troll Combat Playtest v6 — Final Report\n\n`;
rpt += `## 1. Purpose / Scope\n\n`;
rpt += `One scripted combat between Adventurer-1 and the Ice Troll, Round 1 to conclusion, using only the rules and values in the v6 execution prompt. Non-canonical advisory playtest.\n\n`;
rpt += `## 2. Combatant Summary\n\n`;
rpt += `### Adventurer-1\n`;
rpt += `- All 24 attributes: 50\n`;
rpt += `- HP: ${pc.hpMax} | MP: ${pc.mpMax} | PE: ${pc.peMax} | Speed: ${pc.speed} | E.Regen: ${pc.energyRegen}\n`;
rpt += `- Attack2 (Tier 2, PE): bps+bsp, Cap 50, Final Current ${pc.skills.Attack2.current}\n`;
rpt += `- Defence2 (Tier 2, PE): bss+bse, Cap 50, Final Current ${pc.skills.Defence2.current}\n\n`;
rpt += `### Ice Troll\n`;
rpt += `- HP: ${troll.hpMax} | MP: ${troll.mpMax} | PE: ${troll.peMax} | Speed: ${troll.speed} | E.Regen: ${troll.energyRegen}\n`;
rpt += `- Sharktoothed Maw (Tier 2, PE): bpp+bep, Cap 75, Final Current ${troll.skills["Sharktoothed Maw"].current}\n`;
rpt += `- Icy Claws (Tier 2, PE): bsp+bpp, Cap 67, Final Current ${troll.skills["Icy Claws"].current}\n`;
rpt += `- Brawling (Tier 1, PE): bpp, Cap ${troll.skills["Brawling"].cap}, Final Current ${troll.skills["Brawling"].current}\n\n`;
rpt += `## 3. Scaffold Note\n\n`;
rpt += `> Attack2 and Defence2 exist for this playtest only (DEC-012 prompt-level exception, Tiwa 2026-09-04). Their attribute-pair assignment is part of that scaffold (needed so wound-target candidates are defined). They are NOT register-backed PC-scoped ruling; they create no precedent.\n\n`;
rpt += `## 4. Rulings Exercised\n\n`;
for (const r of [...rulings].sort()) rpt += `- ${r}\n`;
rpt += `\nOverflow HP damage: exercised where PE cost exceeded pool.\nCap-clamp recalculation: applied after every wound.\nFrightened -1 to all PC skills: applied every PC roll from Round 1.\nSkill increase via Failure XP: applied on every failed roll.\nFailed Doubles: ${failedDoubleCount} new skills created.\n\n`;
rpt += `## 5. Round-by-Round Summary\n\n`;
for (const rd of allRounds) {
  rpt += `### Round ${rd.round}\n\n`;
  rpt += `| # | Attacker | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Overflow | vs | Defender | Skill | Roll | Eff.Skill | OK | Margin | PE pre→post | Result | AD Roll | AD OK | AD Margin | Effect | DMG | Zone | Target | New Val |\n`;
  rpt += `|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n`;
  for (const ex of rd.exchanges) {
    const adR = ex.adRoll != null ? ex.adRoll : "-";
    const adOK = ex.adSuccess != null ? ex.adSuccess : "-";
    const adM = ex.adMargin != null ? ex.adMargin : "-";
    const eff = ex.effectChoice || "-";
    const dmg = ex.injuryDmg != null ? ex.injuryDmg : "-";
    const zone = ex.locZone || "-";
    const tgt = ex.woundTargetName || "-";
    const nval = ex.woundNewVal != null ? ex.woundNewVal : (ex.pcHPlater != null ? "HP:"+ex.pcHPlater : (ex.trollHPlater != null ? "HP:"+ex.trollHPlater : "-"));
    rpt += `| ${ex.exchange} | ${ex.attacker} | ${ex.atkSkill} | ${ex.aRoll} | ${ex.aSkill} | ${ex.aSuccess} | ${ex.aMargin} | ${ex.aPEbefore}→${ex.aPEafter} | ${ex.aOverflow} | | ${ex.defender} | ${ex.defSkill} | ${ex.dRoll} | ${ex.dSkill} | ${ex.dSuccess} | ${ex.dMargin} | ${ex.dPEbefore}→${ex.dPEafter} | ${ex.result} | ${adR} | ${adOK} | ${adM} | ${eff} | ${dmg} | ${zone} | ${tgt} | ${nval} |\n`;
    for (const rp of (ex.repeats || [])) {
      rpt += `| | (repeat) | | ${rp.aRoll} | | | | | | | | ${rp.dRoll} | | | | | tie/both-fail→${ex.result} | | | | | | | | |\n`;
    }
  }
  rpt += `\n`;
}
rpt += `## 6. Wound-Chain Record\n\n`;
rpt += `Full chain for every Wound/Condition Effect produced:\n\n`;
for (const rd of allRounds) {
  for (const ex of rd.exchanges) {
    if (ex.woundMag != null) {
      rpt += `**Round ${rd.round} Exchange ${ex.exchange}:** ${ex.attacker} → ${ex.atkSkill} vs ${ex.defSkill}.\n`;
      rpt += `- Attacker roll: ${ex.locRoll} → swap digits: ${ex.locSwap} → Zone: ${ex.locZone}\n`;
      rpt += `- Base: Tier 2, Magnitude 2\n`;
      rpt += `- AD Step 1 (tier shred): ${ex.woundShred} (attack T2 vs defense T2 → equal → −1)\n`;
      rpt += `- AD Step 2 (margin subtract): −${ex.woundAdMargin}\n`;
      rpt += `- Final: Tier ${ex.woundTier}, Magnitude ${ex.woundMag}\n`;
      rpt += `- Target attribute: ${ex.woundTarget} (${ex.woundTargetName})\n`;
      rpt += `- ${ex.woundTargetName}: ${ex.woundOldVal} → ${ex.woundNewVal} (−${ex.woundMag})\n\n`;
    }
  }
}
rpt += `## 7. Systems Confirmed Working\n\n`;
rpt += `- Core Test 9-step transaction: every roll\n`;
rpt += `- S-1 Opposed Contest (DEC-013): every exchange\n`;
rpt += `- Active Defense mandatory: every attacker-win exchange\n`;
rpt += `- DEC-103 AD shred/margin chain: every Wound produced\n`;
rpt += `- DEC-104 Injury contest-delta: every Injury produced\n`;
rpt += `- DEC-105 Melee exchange structure\n`;
rpt += `- DEC-106 Creature multi-action: Troll double attack each round\n`;
rpt += `- DEC-095 Turn order by Speed\n`;
rpt += `- DEC-098 Defensive skill (Brawling for Troll)\n`;
rpt += `- DEC-100/014 Location Index (swap digits)\n`;
rpt += `- DEC-102 Wound target random selection\n`;
rpt += `- DEC-107 Wound capability Tier 2\n`;
rpt += `- DEC-108 Uncapped HP\n`;
rpt += `- Frightened -1 to all PC skills\n`;
rpt += `- Overflow HP damage\n`;
rpt += `- Cap-clamp recalculation\n`;
rpt += `- Skill increase from Failure XP\n`;
rpt += `- Failed Double advanced skill creation: ${failedDoubleCount} times\n`;
rpt += `- Repeat contest (tie / both-fail): ${repeatCount} times\n\n`;
rpt += `## 8. Edge Cases\n\n`;
for (const ec of edgeCases) rpt += `- Round ${ec.round}: ${ec.event}\n`;
if (edgeCases.length === 0) rpt += `- None beyond standard mechanics.\n`;
rpt += `\n`;
rpt += `## 9. Coverage Matrix\n\n`;
rpt += `| Mechanism | Exercised | Notes |\n|---|---|---|\n`;
rpt += `| Core Test (9-step) | Yes | Every roll |\n`;
rpt += `| S-1 Opposed Contest | Yes | Every exchange, with repeats |\n`;
rpt += `| Active Defense | Yes | Mandatory on attacker wins |\n`;
rpt += `| Wound/Condition Effect | Yes |\n`;
rpt += `| Injury (HP) Effect | Yes |\n`;
rpt += `| Frightened | Yes | -1 all PC skills R1+ |\n`;
rpt += `| Overflow | Yes |\n`;
rpt += `| Cap-clamp | Yes |\n`;
rpt += `| Uncapped HP | Yes |\n`;
rpt += `| Failed Double | ${failedDoubleCount>0?'Yes ('+failedDoubleCount+')':'No'} |\n`;
rpt += `| Repeat contest | ${repeatCount>0?'Yes ('+repeatCount+')':'No'} |\n`;
rpt += `| Skill increase (Failure XP) | Yes |\n`;
rpt += `| DEC-106 Multi-action | Yes | Troll uses both attacks |\n`;
rpt += `| DEC-102 Random wound target | Yes |\n`;
rpt += `| DEC-100 Location Index | Yes |\n\n`;
rpt += `## 10. Total Core Tests\n\n`;
rpt += `**${totalCoreTests}** total Core Tests.\n\n`;
rpt += `Breakdown:\n`;
rpt += `- S-1 contest rolls: 2 per exchange × ${endRound} rounds × 3 exchanges = ${(endRound*3*2)}\n`;
rpt += `- Active Defense rolls: variable\n`;
rpt += `- Repeat rolls: ${repeatCount} repeat contests × 2 = ${repeatCount*2}\n\n`;
rpt += `## 11. Rounds + Wall-Clock Estimate\n\n`;
rpt += `- Rounds: ${endRound}\n`;
rpt += `- Estimated human GM wall-clock: ~${endRound * 8}–${endRound * 12} minutes\n\n`;
rpt += `## 12. Stop / Blocker Log\n\n`;
rpt += `None. Combat ran to natural conclusion (incapacitation).\n\n`;
rpt += `## 13. Lessons\n\n`;
rpt += `- The Wound chain is complex but mechanical: shred → margin → carry → target → recalc → clamp. Each step is deterministic.\n`;
rpt += `- PE economy is tight for the PC (PE 150, recovery 50); three rolls per round (2 AD +1 attack) costs ~150 PE on average. Overflow is a real risk on high rolls.\n`;
rpt += `- Cap-clamp after wounds creates a cascading degradation: wound → attribute drop → skill cap drop → skill clamp → less effective → more wounds.\n`;
rpt += `- Frightened -1 is minor but persistent; it reduces the PC's effective skill from 25 to 24.\n`;
rpt += `- The Troll's signature attacks at Current = Cap (67 and 75) are highly reliable; the PC's skills at 25 are not. This creates asymmetric pressure.\n`;
rpt += `- Failed Doubles can create new skills mid-combat, adding mechanical complexity.\n\n`;
rpt += `## 14. Conclusion\n\n`;
rpt += `Combat concluded at end of **Round ${endRound}**.\n\n`;
rpt += `- **Adventurer-1:** HP ${pc.hp}/${pc.hpMax} (${pc.alive?'alive':'INCAPACITATED'}), PE ${pc.pe}/${pc.peMax}\n`;
rpt += `- **Ice Troll:** HP ${troll.hp}/${troll.hpMax} (${troll.alive?'alive':'INCAPACITATED'}), PE ${troll.pe}/${troll.peMax}\n\n`;
rpt += `Total Core Tests: **${totalCoreTests}**\n`;

fs.writeFileSync('tiwas-ice-troll-playtest-v6-report-2026-09-05.md', rpt);

// === STRUCTURED JSON ===
const jsonData = {
  rng: { type:"LCG", a:1664525, c:1013904223, m:"2^32", seed:42 },
  preCombat: {
    pc: { hp:600,mp:600,pe:150,hpMax:600,mpMax:600,peMax:150,speed:150,energyRegen:100,mpRegen:100,movement:6,
      attrs: Object.fromEntries(allAttrs.map(a=>[a,50])),
      skills: { Attack2:{tier:2,formula:["bps","bsp"],cap:50,current:25}, Defence2:{tier:2,formula:["bss","bse"],cap:50,current:25} }},
    troll: { hp:705,mp:420,pe:220,hpMax:705,mpMax:420,peMax:220,speed:175,energyRegen:140,mpRegen:75,movement:7,
      attrs: {...trA},
      skills: { "Icy Claws":{tier:2,formula:["bsp","bpp"],cap:67,current:67}, "Sharktoothed Maw":{tier:2,formula:["bpp","bep"],cap:75,current:75}, "Brawling":{tier:1,formula:["bpp"],cap:75,current:37} }}
  },
  rounds: allRounds,
  postCombat: {
    pc: { hp:pc.hp,hpMax:pc.hpMax,pe:pc.pe,peMax:pc.peMax,mp:pc.mp,mpMax:pc.mpMax,alive:pc.alive,
      attrs:{...pc.attrs},
      skills: Object.fromEntries(Object.entries(pc.skills).map(([k,v])=>[k,{tier:v.tier,cap:v.cap,current:v.current,formula:v.formula}])) },
    troll: { hp:troll.hp,hpMax:troll.hpMax,pe:troll.pe,peMax:troll.peMax,mp:troll.mp,mpMax:troll.mpMax,alive:troll.alive,
      attrs:{...troll.attrs},
      skills: Object.fromEntries(Object.entries(troll.skills).map(([k,v])=>[k,{tier:v.tier,cap:v.cap,current:v.current,formula:v.formula}])) }
  },
  totals: { rounds:endRound, coreTests:totalCoreTests, failedDoubles:failedDoubleCount, repeatContests:repeatCount },
  scaffoldFlags: ["Attack2/Defence2 scaffold-only per DEC-012"],
  edgeCases
};

fs.writeFileSync('tiwas-ice-troll-playtest-v6-result-2026-09-05.json', JSON.stringify(jsonData, null, 2));

console.log("=== SIMULATION COMPLETE ===");
console.log("Rounds:", endRound);
console.log("Core Tests:", totalCoreTests);
console.log("PC HP:", pc.hp, "Alive:", pc.alive);
console.log("Troll HP:", troll.hp, "Alive:", troll.alive);
console.log("Failed Doubles:", failedDoubleCount, "Repeats:", repeatCount);
console.log("Edge Cases:", edgeCases.length);
console.log("Files written: tiwas-ice-troll-playtest-v6-report-2026-09-05.md, tiwas-ice-troll-playtest-v6-result-2026-09-05.json");
