---
slug: "nslpi"
url: "/mobilnisite/slovnik/nslpi/"
type: "slovnik"
title: "NSLPI – NAS Signalling Low Priority Indication"
date: 2025-01-01
abbr: "NSLPI"
fullName: "NAS Signalling Low Priority Indication"
category: "Core Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/nslpi/"
summary: "Indikace na úrovni NAS nastavená UE, která signalizuje, že žádost o signalizaci NAS má nízkou prioritu. Používá se při řízení přetížení v síti a umožňuje MME upřednostnit žádosti o signalizaci s vysok"
---

NSLPI je indikace na úrovni NAS nastavená UE, která signalizuje, že žádost o signalizaci NAS má nízkou prioritu. Síť ji využívá pro řízení přetížení, aby upřednostnila kritické procedury.

## Popis

[NAS](/mobilnisite/slovnik/nas/) Signalling Low Priority Indication (NSLPI) je parametr v protokolu Non-Access Stratum (NAS), používaný v systémech EPS (Evolved Packet System) a 5GS. Je zahrnut v určitých žádostních zprávách NAS, jako jsou ATTACH REQUEST, TRACKING AREA UPDATE REQUEST a SERVICE REQUEST, které jsou odesílány z uživatelského zařízení (UE) do Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. NSLPI je jednobitový příznak, který při nastavení informuje síť, že přidružená signalizační procedura může být považována za méně důležitou. Uzel jádra sítě (MME/AMF) používá tuto indikaci jako klíčový vstup pro své mechanismy řízení přetížení a zahlcení. Například, pokud je MME vysokě zatíženo, může zamítnout nebo odložit zpracování požadavků označených NSLPI, zatímco bude nadále přijímat požadavky s vysokou prioritou. UE je povinno nastavit NSLPI pro určité automatizované, uživatelem neiniciované procedury, jako jsou periodické aktualizace oblasti sledování (tracking area) nebo signalizace související se službami snášejícími zpoždění. Mechanismus funguje ve spojení s dalšími funkcemi na úrovni NAS, jako je Attach with [IMSI](/mobilnisite/slovnik/imsi/) a Extended Wait Timer. Když je žádost s nízkou prioritou z důvodu přetížení zamítnuta, síť typicky poskytne UE časovač omezení pokusů (back-off timer, např. T3346), aby zabránila jejímu okamžitému opakování, a tím zmírnila signalizační bouři. Toto end-to-end řízení přetížení na aplikační vrstvě je klíčovým nástrojem pro udržení stability sítě při špičkovém zatížení nebo scénářích selhání.

## K čemu slouží

NSLPI bylo zavedeno k řešení problému signalizačních bouří v řídicí rovině a přetížení jádra sítě, které se staly výraznějšími s rozšířením zařízení M2M a IoT. Rané mobilní sítě byly navrženy především pro komunikaci orientovanou na člověka, kde je signalizace relativně řídká a iniciovaná uživatelem. Příchod milionů IoT zařízení provádějících automatizované periodické registrace a hlášení vytvořil riziko masivní synchronizované signalizační přenosy, která mohla zahltit [MME](/mobilnisite/slovnik/mme/). To mohlo degradovat služby pro všechny uživatele, včetně těch, kteří uskutečňovali nouzová volání. NSLPI poskytuje standardizovaný způsob, jak mohou UE – zejména ta nakonfigurovaná pro služby snášející zpoždění nebo s nízkou prioritou – identifikovat svou signalizaci jako nekritickou. To umožňuje síti implementovat inteligentní řízení přetížení a upřednostňovat nezbytný lidský provoz a kritickou strojovou komunikaci. Řeší tak omezení sítí, které všechny signalizační požadavky považovaly za rovnocenné, což je činilo zranitelnými vůči kolapsu z přetížení v důsledku masivního nasazení IoT. Tato funkce je základním kamenem vylepšení Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)) v 3GPP a umožňuje škálovatelnou podporu obrovského počtu zařízení bez kompromisů v síťové spolehlivosti.

## Klíčové vlastnosti

- Jednobitový indikátor ve zprávách signalizace NAS (např. ATTACH REQUEST) od UE k síti.
- Umožňuje síťovou diferenciaci mezi signalizací řídicí roviny s vysokou a nízkou prioritou.
- Klíčový vstup pro algoritmy řízení přetížení a zahlcení MME/AMF.
- Primárně používán pro zařízení snášející zpoždění a automatizované, uživatelem neiniciované procedury.
- Spouští síťové odezvy, jako je zamítnutí žádosti s prodlouženými časovači čekání, ke snížení signalizační zátěže.
- Zvyšuje odolnost sítě a dostupnost služeb pro nouzové a vysoce prioritní služby během přetížení.

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 27.007** (Rel-19) — AT Command Set for UE

---

📖 **Anglický originál a plná specifikace:** [NSLPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nslpi/)
