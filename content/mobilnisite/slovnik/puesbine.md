---
slug: "puesbine"
url: "/mobilnisite/slovnik/puesbine/"
type: "slovnik"
title: "PUESBINE – Provision of User Equipment Specific Behaviour Information to Network Entities"
date: 2025-01-01
abbr: "PUESBINE"
fullName: "Provision of User Equipment Specific Behaviour Information to Network Entities"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/puesbine/"
summary: "Funkce 3GPP umožňující síti přijímat a využívat informace o specifickém chování UE, jako jsou pohybové vzorce nebo využívání služeb. To umožňuje optimalizovanou správu síťových prostředků, vylepšená r"
---

PUESBINE je funkce 3GPP, která umožňuje síti přijímat a využívat informace o specifickém chování UE (uživatelského zařízení) pro optimalizaci správy prostředků a zlepšení kvality služeb.

## Popis

PUESBINE je funkce správy a optimalizace sítě definovaná ve specifikacích 3GPP. Jejím hlavním účelem je usnadnit přenos dat o chování specifickém pro konkrétní uživatelské zařízení (UE) z tohoto zařízení nebo ze síťového prvku, který takové informace uchovává, k dalším příslušným síťovým funkcím ([NF](/mobilnisite/slovnik/nf/)). Tyto informace nejsou standardním hlášením schopností UE, ale zaměřují se na naučené nebo nakonfigurované vzorce chování. Architektura zahrnuje vylepšení protokolů jádra sítě, zejména těch mezi funkcí správy mobility ([MME](/mobilnisite/slovnik/mme/)) v EPS nebo funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5GC a eNodeB/gNodeB prostřednictvím rozhraní S1-AP nebo [NG-AP](/mobilnisite/slovnik/ng-ap/). Klíčové specifikace jako 23.012 (Správa polohy) a 25.413 (Signalizace [RANAP](/mobilnisite/slovnik/ranap/) na rozhraní Iu [UTRAN](/mobilnisite/slovnik/utran/)) podrobně popisují postupy pro předávání těchto informací.

Mechanismus funguje tak, že umožňuje síti být vybavena behaviorálními parametry nebo je přijímat od UE. Ty mohou zahrnovat očekávané trajektorie mobility (např. pro UE instalované ve vlaku), typické komunikační vzorce nebo specifické požadavky na služby. Tato data jsou pak poskytnuta síťovým entitám, jako je RAN uzel (eNodeB/gNodeB), během procedur jako je počáteční nastavení kontextu nebo příprava předání spojení. RAN může tyto informace využít k proaktivním rozhodnutím; například k předalokaci prostředků podél předpokládané trasy nebo k výběru vhodnější cílové buňky pro předání spojení na základě historického nebo deklarovaného chování UE.

PUESBINE hraje klíčovou roli v přechodu od reaktivní k prediktivní správě sítě. Porozuměním specifickému chování UE může síť optimalizovat přidělování rádiových prostředků, snížit signalizační režii způsobenou zbytečnými měřeními nebo aktualizacemi polohy a zlepšit celkový uživatelský zážitek díky předvídání potřeb. Je to základní koncept pro umožnění efektivnějšího provozu sítě, zejména ve scénářích zahrnujících předvídatelné pohybové vzorce nebo zařízení internetu věcí (IoT) s velmi pravidelnými komunikačními plány. Definice této funkce napříč více vydáními a rozhraními podtrhuje její význam jako nástroje optimalizace napříč doménami.

## K čemu slouží

PUESBINE byl vytvořen k řešení omezení tradiční, reaktivní správy sítě, která zachází se všemi UE víceméně stejně na základě okamžitých rádiových podmínek a standardních schopností. Tento přístup je neefektivní pro zařízení s předvídatelným chováním, což vede ke zbytečné signalizaci, neoptimálnímu využití prostředků a potenciálnímu zhoršení služeb. Primární problém, který řeší, je nedostatek kontextu v síti ohledně zamýšleného nebo historického provozního vzoru UE.

Historicky sítě optimalizovaly pro průměrný případ, ale výkon specializovaných zařízení (jako jsou ta na vozidlech nebo v průmyslové automatizaci) mohl trpět. PUESBINE poskytuje standardizovaný mechanismus pro vložení tohoto behaviorálního kontextu do procesů rozhodování sítě. Jeho vznik byl motivován rostoucí rozmanitostí typů UE a případů užití, zejména s nástupem komunikace mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)), kde zařízení často následují velmi specifické, předvídatelné rutiny. Řešením tohoto problému s kontextem PUESBINE umožňuje významné zvýšení efektivity v řízení mobility a kontrole rádiových prostředků, což je klíčové pro škálovatelnost a výkon sítě.

## Klíčové vlastnosti

- Umožňuje hlášení vzorců chování specifických pro UE k RAN a jádru sítě (CN)
- Podporuje optimalizaci procedur předání spojení na základě předpokládané mobility
- Usnadňuje proaktivní správu rádiových prostředků podél očekávaných tras
- Snižuje signalizační režii sítě pro předvídatelná UE
- Zvyšuje kvalitu služeb (QoS) pro specializované služby poskytnutím kontextu o chování
- Definován napříč specifikacemi více rozhraní jádra sítě a RAN

## Definující specifikace

- **TS 23.012** (Rel-19) — Circuit Switched Location Management Procedures
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description

---

📖 **Anglický originál a plná specifikace:** [PUESBINE na 3GPP Explorer](https://3gpp-explorer.com/glossary/puesbine/)
