---
slug: "n5gc"
url: "/mobilnisite/slovnik/n5gc/"
type: "slovnik"
title: "N5GC – Non-5G Capable"
date: 2025-01-01
abbr: "N5GC"
fullName: "Non-5G Capable"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/n5gc/"
summary: "Indikátor schopnosti sítě nebo zařízení označující absenci podpory systému 5G. Používá se v procedurách výběru sítě, registrace a autorizace služeb pro správu interoperability a záložních mechanismů m"
---

N5GC je indikátor schopnosti sítě nebo zařízení označující absenci podpory systému 5G. Používá se v procedurách, jako je výběr sítě a registrace, pro správu interoperability se staršími systémy.

## Popis

Non-5G Capable (N5GC) je indikátor schopnosti definovaný v architektuře 5G System (5GS) pro označení entit – typicky uživatelského zařízení (UE) nebo síťových uzlů – které nepodporují funkce 5G Core Network (5GC). Tento status je klíčový pro procedury objevování a výběru sítě, zejména během počátečního připojení nebo při událostech mobility. Když UE indikuje N5GC, informuje tím síť, že nemůže využívat protokoly, služby nebo rozhraní specifické pro 5G, jako jsou ty definované pro Service-Based Interface (SBI) architekturu nebo model QoS pro 5G. To spouští v síti mechanismus pro nasměrování UE k příslušné starší síti jádra, jako je Evolved Packet Core (EPC), nebo pro poskytnutí omezeného přístupu ke službám v kontextu 5GS pomocí záložních mechanismů.

Technická implementace N5GC zahrnuje signalizaci v protokolech Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), jak je specifikováno v 3GPP TS 24.501. Během procedur registrace nebo správy relace UE zahrnuje informace o svých schopnostech do zpráv, jako je Registration Request. Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) tyto informace zpracovává. Pokud je indikováno N5GC, může AMF omezit přístup UE k síťovým řezům specifickým pro 5G, zabránit vytvoření PDU Sessions s určitými charakteristikami QoS pro 5G nebo iniciovat přesměrování na EPC pomocí procedur mezisystémové mobility. Síť to využívá k vynucování politik, zajištění kontinuity služeb a efektivní správě rádiových a síťových prostředků jádra tím, že nepřiděluje prostředky vyhrazené pro 5G neschopným zařízením.

Z pohledu síťové architektury hraje N5GC roli ve vzájemném propojení mezi 5GS a Evolved Packet System (EPS). Je to klíčový parametr pro propojení přes rozhraní N26 (pokud je přítomno) a v procedurách předávání a záložních procedurách definovaných mezi 5GC a EPC. Tento koncept zajišťuje zpětnou kompatibilitu a umožňuje postupnou migraci ze sítí 4G na 5G. Zabraňuje nekompatibilním UE v pokusech o procedury, které by selhaly, čímž snižuje signalizační režii a zlepšuje celkovou spolehlivost sítě. Systémy správy také tuto schopnost využívají pro provisionování účastníků a reportování, rozlišují mezi populací zařízení schopných a nezpůsobilých pro 5G pro účely síťového plánování a strategií nabídky služeb.

## K čemu slouží

Indikátor N5GC byl zaveden, aby řešil přechodnou fázi vývoje mobilních sítí, kdy jsou sítě 5G nasazovány vedle stávajících sítí 4G LTE. Jeho primárním účelem je bezproblémově spravovat koexistenci zařízení a síťových prvků schopných a nezpůsobilých pro 5G. Bez takového indikátoru schopnosti by se procedury výběru sítě a připojení mohly stát neefektivními nebo by selhávaly, protože sítě 5G by mohly nesprávně předpokládat podporu pokročilých funkcí u všech připojujících se zařízení. To by mohlo vést k výpadkům služeb, zvýšené signalizační zátěži z neúspěšných procedur a špatné uživatelské zkušenosti během dlouhého období heterogenního nasazení sítě.

Historicky podobné indikátory schopností existovaly pro přechody mezi sítěmi 2G/3G a 4G. Vytvoření N5GC pokračuje v tomto vzoru, konkrétně pro éru 5G definovanou od 3GPP Release 15 dále. Řeší problém jasné dohody o schopnostech, což umožňuje síťovým operátorům implementovat šetrné záložní politiky. Například starší zařízení IoT nebo starší model smartphonu může stále získávat základní konektivitu přes sítě 4G, zatímco je identifikováno jako N5GC, což zajišťuje, že nespotřebovává prostředky specifické pro 5G ani nespouští nepodporované síťové funkce. To operátorům umožňuje optimalizovat jejich investice do 5G tím, že vyhradí prostředky 5G pro zařízení, která je mohou skutečně využít, a zároveň zachovávají služby pro velkou instalovanou základnu zařízení před érou 5G.

Dále N5GC podporuje regulatorní a servisní požadavky tím, že zajišťuje, aby nouzové služby nebo povinná komunikace nebyly omezeny neshodou schopností. Umožňuje síti aplikovat správná pravidla politiky a účtování na základě schopnosti zařízení podporovat síť jádra. Indikátor je zásadní pro úspěch síťového řezání, protože řez určený pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) by byl nevhodný pro zařízení s N5GC. Jeho účel tedy přesahuje pouhou kompatibilitu a umožňuje efektivní správu prostředků, diferenciaci služeb a řízenou migrační cestu k plnohodnotnému nasazení 5G.

## Klíčové vlastnosti

- Indikuje nedostatek podpory protokolů 5G Core Network v UE nebo síťových entitách
- Používá se v NAS signalizaci během procedur registrace a správy relace
- Spouští síťově řízené přepnutí (fallback) na Evolved Packet Core (EPC) pro přístup
- Ovlivňuje výběr síťového řezu a jeho dostupnost pro zařízení
- Umožňuje efektivní mezisystémovou mobilitu mezi 5GS a EPS
- Podporuje reportování pro správu účastníků a zařízení při síťovém plánování

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.571** (Rel-19) — Common Data Types for 5G Service Based Interfaces

---

📖 **Anglický originál a plná specifikace:** [N5GC na 3GPP Explorer](https://3gpp-explorer.com/glossary/n5gc/)
