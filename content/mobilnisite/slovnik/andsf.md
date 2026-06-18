---
slug: "andsf"
url: "/mobilnisite/slovnik/andsf/"
type: "slovnik"
title: "ANDSF – Access Network Discovery and Selection Function"
date: 2025-01-01
abbr: "ANDSF"
fullName: "Access Network Discovery and Selection Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/andsf/"
summary: "ANDSF je síťová funkce, která poskytuje mobilním zařízením politiky a informace pro vyhledání a výběr ne-3GPP přístupových sítí, jako je Wi-Fi. Umožňuje inteligentní směrování provozu a bezproblémovou"
---

ANDSF je síťová funkce, která poskytuje mobilním zařízením politiky a informace pro vyhledání a výběr ne-3GPP přístupových sítí, jako je Wi-Fi, a umožňuje inteligentní směrování provozu mezi typy sítí.

## Popis

Access Network Discovery and Selection Function (ANDSF) je prvek jádra sítě definovaný 3GPP pro správu konektivity uživatelského zařízení (UE) napříč heterogenními rádiovými přístupovými technologiemi. Jeho hlavní úlohou je pomáhat UE při vyhledávání dostupných ne-3GPP přístupových sítí (jako [WLAN](/mobilnisite/slovnik/wlan/)/Wi-Fi) a poskytovat jim politiky výběru sítě a směrování provozu definované operátorem. ANDSF komunikuje s UE prostřednictvím rozhraní založeného na IP, typicky pomocí protokolu [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/) (Open Mobile Alliance Device Management) nebo pozdějších mechanismů založených na [HTTP](/mobilnisite/slovnik/http/), aby tyto politiky bezpečně poskytovalo a aktualizovalo. Funguje jako úložiště politik a systém pro podporu rozhodování, centralizující pravidla operátora pro odlehčování provozu (offloading) a mobilitu.

Architektonicky je ANDSF samostatný server v IP síti operátora, často integrovaný s Evolved Packet Core (EPC). Obsahuje dvě hlavní datové složky: Informace o objevení (Discovery Information) a Politiky mobility mezi systémy (Inter-System Mobility Policies, [ISMP](/mobilnisite/slovnik/ismp/)). Informace o objevení poskytují UE seznam dostupných přístupových sítí v jeho okolí, včetně jejich identifikátorů ([SSID](/mobilnisite/slovnik/ssid/), [HESSID](/mobilnisite/slovnik/hessid/)) a údajů o geografické poloze. Politiky mobility mezi systémy (ISMP) jsou pravidla, která určují, jak má UE vybrat přístupový bod, když je k dispozici více možností, na základě kritérií jako denní doba, poloha uživatele a rádiové podmínky. Třetí složka, Politiky směrování mezi systémy (Inter-System Routing Policies, [ISRP](/mobilnisite/slovnik/isrp/)), definuje, jak mají být směrovány konkrétní IP toky (např. video stream), což může umožňovat současná připojení přes 3GPP a WLAN.

ANDSF funguje ve dvou hlavních režimech: režim vyžádání (pull mode), kdy UE žádá o informace, a režim zaslání (push mode), kdy ANDSF iniciuje aktualizaci politik směrem k UE. V režimu vyžádání odešle UE žádost obsahující svou polohu, schopnosti a stav aktuální přístupové sítě. ANDSF tuto žádost zpracuje, vyhodnotí příslušné politiky a vrátí relevantní Informace o objevení, ISMP a/nebo ISRP. Tyto politiky jsou formátovány pomocí standardizované struktury Management Object (MO) definované ve specifikacích 3GPP. Klient ANDSF v UE pak tyto politiky spolu s místními uživatelskými preferencemi a měřeními rádiového rozhraní v reálném čase použije k provedení konečného rozhodnutí o výběru sítě a směrování provozu.

Jeho role přesahuje pouhé vyhledávání; je klíčovým prvkem pro směrování provozu, vyrovnávání zatížení a bezproblémové vertikální předávání hovorů. Tím, že poskytuje centralizovanou, dynamickou správu politik, umožňuje ANDSF operátorům optimalizovat kapacitu sítě, snížit přetížení v celulárních sítích a zajistit, aby byli uživatelé připojeni k nejlepší dostupné síti podle požadavků jejich služeb. Tvoří kritickou část širšího rámce správy mobility založeného na síti a spolupracuje s dalšími prvky EPC, jako je PCRF (Policy and Charging Rules Function), pro integrované politiky kvality služeb (QoS) a účtování napříč typy přístupu.

## K čemu slouží

ANDSF bylo vytvořeno, aby řešilo rostoucí potřebu inteligentní integrace a správy heterogenních sítí, konkrétně konvergence 3GPP celulárních sítí (jako LTE) a ne-3GPP bezdrátových přístupových technologií, především IEEE 802.11 (Wi-Fi). Před zavedením ANDSF bylo vyhledávání a výběr sítě z velké části záležitostí UE a neřízené. Zařízení autonomně skenovala a připojovala se k Wi-Fi sítím na základě jednoduché síly signálu nebo uživatelských preferencí, bez možnosti dohledu nebo kontroly ze strany mobilního operátora. To vedlo k neoptimálnímu využití sítě, potenciálním bezpečnostním rizikům na nedůvěryhodných sítích a k roztříštěnému uživatelskému zážitku při pohybu mezi celulární sítí a Wi-Fi.

Hlavním problémem, který ANDSF řeší, je poskytnutí kontroly operátora v prostředí s více přístupy. Bez něj nemohli operátoři předvídatelně směrovat provoz za účelem odlehčení kapacity z přetížených celulárních pásem na dostupné Wi-Fi zdroje. Také jim chyběla schopnost vynucovat politiky, které by mohly upřednostňovat určité služby nebo zajišťovat bezproblémovou kontinuitu služeb. Vznik ANDSF byl motivován snahou učinit z Wi-Fi řízené rozšíření mobilní širokopásmové sítě, nikoli konkurenční, nekoordinovanou přístupovou metodu. Umožňuje operátorům implementovat obchodní pravidla, jako je odlehčování provozu typu best-effort na Wi-Fi při zachování citlivého hlasového provozu s nízkou latencí na LTE, nebo poskytování bezproblémového přístupu k Wi-Fi hotspotům vlastněným operátorem.

Historicky zavedené v 3GPP Release 8 spolu s architekturou SAE/EPC, vznik ANDSF byl hnán posunem průmyslu směrem k plně IP sítím a uznáním, že budoucí růst mobilních dat bude vyžadovat agregaci různorodých rádiových technologií. Řešilo omezení předchozích neintegrovaných přístupů standardizací bezpečného, politikami řízeného rámce pro vyhledávání a výběr přístupové sítě. To umožnilo nové případy užití, jako je mobilita řízená sítí, optimalizovaná alokace zdrojů a základ pro pozdější vylepšení, jako je bezproblémové odlehčování na WLAN a integrace s principy 5G jádra sítě.

## Klíčové vlastnosti

- Poskytuje standardizované Politiky mobility mezi systémy (ISMP) pro výběr sítě
- Dodává Informace o objevení včetně identifikátorů WLAN a geografických oblastí
- Definuje Politiky směrování mezi systémy (ISRP) pro směrování provozu založené na tocích
- Podporuje jak poskytování politik iniciované UE (pull), tak iniciované sítí (push)
- Umožňuje kontrolu operátora nad odlehčováním provozu mezi 3GPP a WLAN sítěmi
- Využívá protokoly OMA DM nebo HTTP pro bezpečný přenos politik

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [WLAN – Wireless Local Area Network](/mobilnisite/slovnik/wlan/)
- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS
- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [ANDSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/andsf/)
