---
slug: "dm"
url: "/mobilnisite/slovnik/dm/"
type: "slovnik"
title: "DM – Disconnected Mode"
date: 2025-01-01
abbr: "DM"
fullName: "Disconnected Mode"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/dm/"
summary: "Typ rámce v protokolech 3GPP označující stav, kdy je spojení logicky zachováno, ale fyzický přenosový kanál je neaktivní. Je klíčový pro úsporu energie a efektivní správu zdrojů, protože umožňuje zaří"
---

DM je typ rámce označující stav, kdy je spojení logicky zachováno, ale fyzický přenosový kanál je neaktivní; používá se pro úsporu energie a efektivní správu zdrojů.

## Popis

Disconnected Mode (DM) je základní typ rámce a provozní stav definovaný v řadě specifikací 3GPP, především v kontextu protokolů vrstvy datového spoje. Představuje stav, kdy je logické spojení mezi dvěma partnerskými entitami (např. mezi uživatelským zařízením (UE) a sítí nebo mezi síťovými uzly) zachováno, ale aktivní přenos uživatelských dat je pozastaven. Fyzické prostředky spojené se spojením mohou být uvolněny, ale kontext a konfigurační parametry jsou zachovány na obou koncích. Tento stav se liší od úplného uvolnění spojení nebo stavu nečinnosti (idle), protože umožňuje rychlejší obnovení přenosu dat v případě potřeby a vyhýbá se plné signalizační režii spojené s novým navázáním spojení.

Z architektonického hlediska je DM implementován v rámci protokolových vrstev, jako je Radio Link Control (RLC) a Packet Data Convergence Protocol (PDCP) na rozhraní rádiového přístupu, a podobné koncepty existují v signalizačních protokolech jádra sítě. Do tohoto režimu se typicky vstupuje prostřednictvím explicitního řídicího postupu, jako je procedura Suspend nebo Inactivity, spuštěného po uplynutí nastaveného časovače při absenci datové aktivity. Zatímco je zařízení nebo síťový uzel v DM, může vypnout příslušné rádiové komponenty nebo procesní jednotky, aby šetřil energii, a zároveň periodicky monitorovat volací (paging) nebo spouštěcí zprávy, které signalizují potřebu obnovit spojení.

Klíčové komponenty umožňující DM zahrnují logiku správy stavu v rámci stavových automatů protokolu, časovače řídící detekci nečinnosti a přechody mezi stavy a mechanismy pro zachování kontextu. Zachovaný kontext zahrnuje bezpečnostní klíče, konfiguraci přenosových kanálů (bearer), IP adresy a profily kvality služeb (QoS). Role DM v síti je mnohostranná: je základním kamenem pro úsporu energie zařízení, zejména pro uživatelská zařízení (UE) napájená z baterií, a je kritická pro efektivní správu rádiových prostředků. Tím, že síti umožní rychle získat zpět fyzické prostředky (jako jsou časově-frekvenční bloky nebo kanalizační kódy), a přitom si udržet logický zástup pro spojení, se zvyšuje celková kapacita systému. Obnovení z DM do stavu aktivního přenosu dat zahrnuje proceduru reaktivace, která má výrazně menší signalizační režii než kompletní nastavení ze stavu nečinnosti, čímž se snižuje latence pro aplikace s přerušovaným (bursty) datovým provozem.

## K čemu slouží

Primárním účelem Disconnected Mode je optimalizovat využití síťových prostředků a prodloužit životnost baterie zařízení. V dřívějších mobilních systémech bylo zařízení buď plně připojené (spotřebovávalo rádiové prostředky a energii), nebo zcela v nečinnosti (idle), což vyžadovalo zdlouhavý nastavovací postup pro obnovení. Tento binární přístup byl neefektivní pro aplikace s přerušovaným, bursty datovým provozem, jako je prohlížení webu, instant messaging nebo push e-mail. DM byl zaveden, aby vytvořil mezilehlý stav s nízkou režií, který vyvažuje kompromis mezi rychlým obnovením spojení a úsporou prostředků.

Historicky vycházela motivace z potřeby zlepšit uživatelský zážitek u paketových služeb v systémech 3G (UMTS) a jejich vývojových verzích. Bez DM by zařízení buď rychle vybila baterii setrváním v trvale připojeném stavu, nebo by trpěla vysokou latencí při přechodu ze stavu nečinnosti do aktivního. DM to řeší tím, že umožňuje síti pozastavit spojení během období nečinnosti, a přitom zachovat potřebný kontext relace. Tím se vyřešila omezení předchozích přístupů, kterým chyběl takto elegantní mechanismus pozastavení a obnovení s uchováním kontextu.

Navíc DM umožňuje sofistikovanější správu mobility a stavů řízenou sítí. Umožňuje síti efektivně spravovat velký počet zařízení z hlediska prostředků, což se stalo stále důležitějším s nástupem aplikací vždy připojených (always-on) a později zařízení internetu věcí (IoT). Standardizací typu rámce DM a souvisejících procedur napříč více specifikacemi zajistilo 3GPP interoperabilitu a konzistentní chování pro úsporu energie a rychlou reaktivaci spojení napříč různými generacemi technologií od 3G po 5G.

## Klíčové vlastnosti

- Zachování kontextu (bezpečnostních klíčů, parametrů QoS a přenosových kanálů) během pozastavení
- Explicitní řídicí procedury pro vstup do režimu a jeho opuštění (např. Suspend/Resume)
- Spouštění přechodu do DM na základě časovače při nečinnosti
- Snížená signalizační režie pro reaktivaci spojení ve srovnání s kompletním nastavením
- Umožňuje významnou úsporu energie uživatelského zařízení (UE) díky možnosti deaktivace rádiových komponent
- Umožňuje síti přerozdělit prostředky fyzické vrstvy při zachování logické relace

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.166** (Rel-19) — IMS Conferencing Management Object
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 24.275** (Rel-19) — MO for MMTEL Basic Communication Part
- **TS 24.285** (Rel-19) — Allowed CSG List Management Object
- **TS 24.286** (Rel-19) — 3GPP TS 24.286: ICS Management Object
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.305** (Rel-19) — Selective Disabling of 3GPP UE Capabilities
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 24.323** (Rel-19) — IMS Service Level Tracing Management Object
- **TS 24.368** (Rel-19) — NAS Configuration Management Object
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [DM na 3GPP Explorer](https://3gpp-explorer.com/glossary/dm/)
