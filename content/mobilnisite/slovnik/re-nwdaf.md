---
slug: "re-nwdaf"
url: "/mobilnisite/slovnik/re-nwdaf/"
type: "slovnik"
title: "RE-NWDAF – Roaming Exchange Network Data Analytics Function"
date: 2026-01-01
abbr: "RE-NWDAF"
fullName: "Roaming Exchange Network Data Analytics Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/re-nwdaf/"
summary: "Specializovaná funkce Network Data Analytics Function (NWDAF) nasazená v rámci platformy roamingové výměny. Shromažďuje a analyzuje síťová a účastnická data z více navštívených a domovských sítí za úč"
---

RE-NWDAF (rE-NWWDAF) je specializovaná funkce NWDAF nasazená v roamingové výměně, která analyzuje data z více sítí za účelem získání přehledů pro optimalizaci roamingových služeb, detekci podvodů a kvalitu uživatelského zážitku (QoE).

## Popis

Roaming Exchange Network Data Analytics Function (RE-NWDAF) je variantou nasazení standardní 3GPP funkce [NWDAF](/mobilnisite/slovnik/nwdaf/), přizpůsobenou pro prostředí roamingové výměny. NWDAF je funkce jádra 5G sítě definovaná pro sběr dat a analytiku. RE-NWDAF je konkrétně instanciována v infrastruktuře poskytovatele roamingové výměny (známého také jako Data Clearing House nebo [IPX](/mobilnisite/slovnik/ipx/) provider), který se nachází mezi domovskou veřejnou pozemní mobilní sítí ([HPLMN](/mobilnisite/slovnik/hplmn/)) a navštívenou [PLMN](/mobilnisite/slovnik/plmn/) ([VPLMN](/mobilnisite/slovnik/vplmn/)). Jejím hlavním úkolem je získání uceleného pohledu na roamingový provoz a výkon napříč operátory, který není viditelný pro NWDAF žádného jednotlivého operátora.

Z architektonického hlediska RE-NWDAF komunikuje s různými síťovými funkcemi a zdroji dat v celém roamingovém ekosystému. To zahrnuje sběr dat z vlastních systémů roamingové výměny (např. přenosových bodů signalizace pro Diameter a [HTTP](/mobilnisite/slovnik/http/)/2), stejně jako potenciální odběr analytických událostí od NWDAF v HPLMN a VPLMN (prostřednictvím služby Nnwdaf_EventsMonitoring). Může pojmout širokou škálu datových typů: signalizační zprávy (např. Nudm, Npcf, Namf), události uživatelské roviny, události řízení politik a měření výkonu související s roamingovými relacemi.

RE-NWDAF na tento federovaný soubor dat aplikuje modely strojového učení ([ML](/mobilnisite/slovnik/ml/)) a analytickou logiku. Funguje tak, že koreluje události z pohledu domovské i navštívené sítě pro stejnou účastnickou relaci. To jí umožňuje generovat jedinečné přehledy, jako je kvalita uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) na koncích pro roamingového uživatele, identifikaci anomálií nebo podvodných vzorců zasahujících více sítí (např. útoky simultánní registrace) a analytiku trendů roamingového provozu a jeho špiček. Může poskytovat své analytické výstupy vlastním provozním systémům roamingové výměny nebo je zpřístupňovat jako službu odběratelským síťovým operátorům prostřednictvím standardizovaných rozhraní, čímž jim pomáhá optimalizovat roamingové dohody a řešit problémy s přeshraničními službami.

## K čemu slouží

RE-NWDAF byla zavedena, aby řešila specifické výzvy analytiky dat v globálním roamingovém ekosystému. V samostatném roamingu 5G mají domovské a navštívené sítě omezený přehled o vzájemných doménách. NWDAF domovského operátora vidí pouze řídicí rovinu domovské sítě a agregované reporty, zatímco NWDAF navštívené sítě vidí pouze svůj lokální kontext. To vytváří slepé místo pro zajištění služeb na koncích, správu podvodů a optimalizaci roamingového zážitku.

Tradiční roamingová analytika spoléhala na offline zpracování fakturačních záznamů (souborů TAP) nebo signalizačních dat z pohledu jedné sítě, což bylo pomalé a neúplné. Motivací pro RE-NWDAF je potřeba získávat inteligenci napříč operátory v reálném čase pro podporu pokročilých roamingových služeb 5G, síťového řezání přes hranice a přísných smluv o úrovni služeb (SLA). Díky využití jedinečné pozice roamingové výměny jako uzlu pro provoz mezi operátory může RE-NWDAF syntetizovat úplný obraz. Řeší problémy, jako je diagnostika hlavní příčiny přerušení roamingové relace (byla v HPLMN, VPLMN nebo v propojení?), detekce sofistikovaných podvodů využívajících jurisdikční mezery, a poskytuje přehledy založené na datech pro vyjednávání a monitorování roamingových partnerství.

## Klíčové vlastnosti

- Agregace dat napříč operátory z pohledu HPLMN i VPLMN
- Analytika roamingové signalizace a dat uživatelské roviny v reálném čase
- Generování přehledů pro roamingový QoE, detekci podvodů a optimalizaci provozu
- Integrace s platformami roamingové výměny (IPX/Data Clearing)
- Podpora pro zpřístupnění analytiky systémům roamingové výměny i operátorským NWDAF
- Korelace dat účastnické relace napříč více síťovými doménami

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [IPX – Internetwork Packet Exchange](/mobilnisite/slovnik/ipx/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)

## Definující specifikace

- **TS 23.288** (Rel-20) — 5GS Architecture Enhancements for Data Analytics
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows

---

📖 **Anglický originál a plná specifikace:** [RE-NWDAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/re-nwdaf/)
