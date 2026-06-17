---
slug: "4g-guti"
url: "/mobilnisite/slovnik/4g-guti/"
type: "slovnik"
title: "4G-GUTI – 4G-Globally Unique Temporary Identifier"
date: 2025-01-01
abbr: "4G-GUTI"
fullName: "4G-Globally Unique Temporary Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/4g-guti/"
summary: "Dočasný identifikátor přidělený uživatelskému zařízení (UE) v sítích 5G, které se původně registrovalo přes 4G E-UTRAN. Umožňuje jádru sítě 5G (5G Core) jedinečně identifikovat a spravovat UE, která p"
---

4G-GUTI je dočasný identifikátor přidělený v sítích 5G pro jedinečnou správu uživatelského zařízení (UE), které se původně registrovalo přes síť 4G, a který chrání jeho trvalou identitu při pohybu mezi různými rádiovými technologiemi (inter-RAT mobility).

## Popis

4G-GUTI je klíčový identifikátor v architektuře systému 5G (5GS), který slouží uživatelským zařízením (UE), jež provedla pohyb mezi rádiovými technologiemi (inter-RAT mobility) ze systému 4G Evolved Packet System (EPS) do 5GS. Vytváří jej funkce pro správu přístupu a mobility (AMF) při registraci UE v jádru sítě 5G (5GC) za použití přihlašovacích údajů a procedur ze sítě 4G, konkrétně během procedury Attach při mobilitě z EPS do 5GS. Identifikátor se skládá ze dvou hlavních částí: Globálně Jedinečného Identifikátoru AMF (GUAMI) a Dočasného Identifikátoru Mobilního Účastníka pro 5G (5G-TMSI). Část GUAMI identifikuje konkrétní AMF, která 4G-GUTI přidělila, zatímco 5G-TMSI je jedinečný identifikátor v kontextu této AMF.

Když se UE poprvé připojí k 5GS přes E-UTRAN (4G rádio), poskytne své přihlašovací údaje založené na 4G, typicky včetně 4G GUTI ze systému EPS. AMF následně tomuto UE přidělí 4G-GUTI, který slouží jako jeho dočasná identita v rámci 5GS. K tomuto přidělení dochází během registrační procedury a je UE sděleno v Registration Accept zprávě. 4G-GUTI je uložen v nevolatilní paměti UE společně s jeho 5G-GUTI, což umožňuje UE používat kterýkoli z těchto identifikátorů v závislosti na přístupové síti a kontextu registrace.

Primární technickou funkcí 4G-GUTI je umožnit AMF jedinečně identifikovat UE, která provedla mobilitu z EPS do 5GS, aniž by bylo nutné, aby tato UE získala nativní 5G-GUTI. Když takové UE zahájí komunikaci v 5GS, zahrne 4G-GUTI do úvodní NAS zprávy, což AMF umožní získat kontext UE z její databáze. AMF udržuje mapování mezi 4G-GUTI a úplnými daty předplatného UE, včetně bezpečnostního kontextu a parametrů mobility. Tento mechanismus je obzvláště důležitý při předávání spojení (handover) mezi sítěmi 4G a 5G, protože umožňuje plynulou kontinuitu služeb bez nutnosti opětovného ověřování nebo kompletní nové registrace.

Z bezpečnostního hlediska slouží 4G-GUTI stejnému základnímu účelu jako jiné dočasné identifikátory v mobilních sítích: chrání trvalý identifikátor předplatného uživatele (SUPI) před přenosem přes rádiové rozhraní, čímž zvyšuje soukromí a bezpečnost. 4G-GUTI může být periodicky nebo při specifických událostech (jako jsou handovery mezi AMF) přidělen znovu, aby se zvýšila bezpečnost prostřednictvím aktualizace identifikátoru. AMF spravuje životní cyklus 4G-GUTI, včetně přidělování, opětovného přidělování a zneplatňování, a zajišťuje, aby každý identifikátor zůstal jedinečný ve svém provozním kontextu a časovém okně.

## K čemu slouží

4G-GUTI byl vytvořen pro řešení specifických požadavků mobility mezi rádiovými technologiemi (inter-RAT) mezi systémem 4G EPS a 5GS, zejména během přechodného období, kdy by mnoho UE přistupovalo k sítím 5G pomocí přihlašovacích údajů a procedur ze sítě 4G. S nasazením sítí 5G vznikla potřeba podporovat UE, která se mohou připojit k 5GC přes 4G rádio (E-UTRAN) i 5G rádio (NG-RAN), což vyžadovalo konzistentní identifikační mechanismus fungující napříč oběma typy přístupu. 4G-GUTI to umožňuje tím, že poskytuje dočasný identifikátor, který propojuje systémy identit 4G a 5G.

Před érou 5G byly dočasné identifikátory specifické pro každou generaci (např. 4G GUTI pro EPS, 3G P-TMSI pro UMTS). Tento přístup vytvářel výzvy pro mobilitu mezi generacemi, protože UE pohybující se mezi systémy často potřebovala získat nové dočasné identifikátory prostřednictvím kompletních registračních procedur. 4G-GUTI to řeší tím, že umožňuje UE, která se registrovala pomocí procedur 4G, zachovat si konzistentní dočasnou identitu při provozu v 5GS, čímž se snižuje signalizační režie a zlepšuje výkon mobility. To bylo obzvláště důležité pro raná nasazení 5G, kde mnoho UE podporovalo schopnosti jádra sítě 5G, ale přistupovalo přes 4G radiovou infrastrukturu.

Vytvoření 4G-GUTI také řešilo obavy o soukromí a bezpečnost specifické pro scénáře inter-RAT. Tím, že umožňuje UE používat dočasný identifikátor odvozený od jejich registračního kontextu v 4G, systém zabraňuje nutnosti přenášet trvalé identifikátory specifické pro 5G přes 4G rádiové spoje, a zachovává tak ochranu soukromí zavedenou v obou systémech. Tento přístup také umožňuje efektivnější předávání spojení (handover) mezi sítěmi 4G a 5G, protože síť může rychle identifikovat a ověřit UE na základě jejich 4G-GUTI, aniž by vyžadovala plné 5G ověřovací procedury pokaždé, když se mezi systémy přesunou.

## Klíčové vlastnosti

- Umožňuje jedinečnou identifikaci UE v 5GS, které se registrovaly přes 4G E-UTRAN.
- Chrání trvalý identifikátor účastníka (SUPI) před odhalením na rádiovém rozhraní.
- Podporuje plynulou mobilitu mezi rádiovými technologiemi (inter-RAT) mezi 4G EPS a 5GS.
- Skládá se ze složek GUAMI a 5G-TMSI pro hierarchickou identifikaci.
- Přiděluje jej AMF během registračních procedur z EPS do 5GS.
- Je uložen spolu s 5G-GUTI v UE pro provoz v duálním systému.

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3

---

📖 **Anglický originál a plná specifikace:** [4G-GUTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/4g-guti/)
