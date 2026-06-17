---
slug: "hrnn"
url: "/mobilnisite/slovnik/hrnn/"
type: "slovnik"
title: "HRNN – Human Readable Network Name"
date: 2025-01-01
abbr: "HRNN"
fullName: "Human Readable Network Name"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hrnn/"
summary: "Textový řetězec zobrazovaný na uživatelském zařízení (UE) k identifikaci obsluhované veřejné pozemní mobilní sítě (PLMN) nebo neveřejné sítě (NPN). Poskytuje uživatelsky přívětivý název sítě (např. „C"
---

HRNN je uživatelsky přívětivý textový řetězec zobrazovaný na zařízení k identifikaci obsluhované veřejné nebo neveřejné mobilní sítě, například „Company 5G Private Network“, namísto pouhých numerických kódů.

## Popis

Human Readable Network Name (HRNN, uživatelsky čitelný název sítě) je síťový identifikátor definovaný ve specifikacích 3GPP pro uživatelsky přívětivé vyhledávání a výběr sítě. Jedná se o řetězec znaků kódovaný v UTF-8, který reprezentuje název sítě, například značku veřejného operátora (např. „Operator A 5G“) nebo privátní/podnikovou síť (např. „Factory Campus Network“). HRNN je vysílán sítí v blocích systémových informací (SIB) přes rádiové rozhraní a je používán UE k prezentaci dostupných sítí uživateli srozumitelným způsobem. Z architektonické perspektivy je HRNN asociován s PLMN ID ([MCC](/mobilnisite/slovnik/mcc/)+[MNC](/mobilnisite/slovnik/mnc/)) nebo s Network Identifier ([NID](/mobilnisite/slovnik/nid/)) pro SNPN (Standalone Non-Public Network). Funguje v rámci procedur Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a Access Stratum ([AS](/mobilnisite/slovnik/as/)) pro výběr a registraci sítě.

Mechanismus funguje následovně: Síť (gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE) zahrnuje HRNN do specifických zpráv systémových informací, jako je SIB1. Když UE provádí počáteční výběr buňky nebo skenuje dostupné sítě, přečte tyto vysílané zprávy. Vrstva NAS v UE přijme HRNN spolu s PLMN ID/NID. Řídící vrstva ([MM](/mobilnisite/slovnik/mm/)) zařízení nebo uživatelské rozhraní pak použije tento HRNN k naplnění seznamu dostupných sítí zobrazeného uživateli. Pro automatický výběr sítě může UE použít PLMN ID ze svého seznamu preferovaných sítí, ale HRNN zlepšuje zážitek z manuálního výběru. V případě neveřejných sítí ([NPN](/mobilnisite/slovnik/npn/)) je HRNN obzvláště důležitý, protože tyto sítě nemusí mít globálně unikátní PLMN ID a jsou určeny pro privátní použití; rozeznatelný název je nezbytný, aby uživatelé dokázali identifikovat a připojit se ke správné privátní síti v prostředích, kde může být přítomno více takových sítí.

HRNN je definován napříč více specifikacemi 3GPP, pokrývajícími aspekty jádra sítě (TS 23.003), řídicí příkazy pro UE (TS 27.007) a procedury rádiového přístupu k síti (TS 38.300, 38.304, 38.331). Jeho zavedení formalizuje dříve existující, avšak výrobci specificky implementovanou praxi, a zajišťuje interoperabilitu. Je specifikováno chování UE při zacházení s HRNN, včetně scénářů, kdy HRNN není poskytnut (UE může zobrazit PLMN ID) nebo kdy jsou vysílány vícejazyčné varianty HRNN (UE vybere nejvhodnější na základě svého nastavení). Tento identifikátor hraje klíčovou roli ve zlepšení uživatelského zážitku, zejména v kontextu síťových řezů a privátních sítí, kde je jasná identifikace nezbytná jak pro spotřebitele, tak pro podnikové uživatele.

## K čemu slouží

HRNN byl zaveden, aby vyřešil problém uživatelského zážitku při identifikaci sítí pouze podle jejich numerických PLMN kódů (MCC+MNC), které jsou pro koncové uživatele nesrozumitelné. Zatímco PLMN ID jsou nezbytná pro směrování v síti a funkce jádra sítě, poskytují nevyhovující rozhraní pro lidskou interakci. Před standardizací některá zařízení a sítě používala proprietární metody pro zobrazení názvů sítí, což vedlo k nekonzistentnostem. Rozmach nových typů sítí v 5G, zejména neveřejných sítí (NPN) a síťových řezů prezentovaných jako virtuální sítě, vytvořil naléhavou potřebu standardizovaného, lidem srozumitelného identifikátoru.

Primární motivací byla podpora vize 5G pro vertikální průmysly a privátní sítě. V továrně, letišti nebo na kampusu může koexistovat více privátních sítí od různých dodavatelů nebo pro různé účely. Technik nebo IoT zařízení potřebuje snadno identifikovat a připojit se k síti „Logistics 5G“ namísto „Security Camera Network“. Spoléhání se na nesrozumitelné numerické kódy by bylo náchylné k chybám a neefektivní. HRNN standardizuje tuto možnost pojmenování a zajišťuje, že jakékoli kompatibilní UE dokáže správně zobrazit název sítě poskytnutý jakýmkoli kompatibilním RAN. Také připravuje systém na budoucí, složitější scénáře výběru sítě zahrnující názvy specifické pro síťové řezy nebo uživatelsky specifická síťová předplatná, čímž zlepšuje použitelnost v rostoucí heterogenní ekosystému 5G.

## Klíčové vlastnosti

- Řetězec znaků kódovaný v UTF-8 pro podporu mezinárodních jazyků
- Vysílán v systémových informacích (např. SIB1) přístupovou sítí (RAN)
- Asociován s PLMN ID pro veřejné sítě nebo s NID pro SNPN
- Používán pro manuální výběr sítě a zobrazení na uživatelských rozhraních UE
- Podporuje více jazykových variant pro stejnou síť
- Zvyšuje použitelnost pro identifikaci a výběr neveřejné sítě (NPN)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [HRNN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hrnn/)
