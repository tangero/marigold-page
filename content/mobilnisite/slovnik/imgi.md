---
slug: "imgi"
url: "/mobilnisite/slovnik/imgi/"
type: "slovnik"
title: "IMGI – International Mobile Group Identity"
date: 2025-01-01
abbr: "IMGI"
fullName: "International Mobile Group Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imgi/"
summary: "IMGI je jedinečný identifikátor používaný primárně v sítích GSM a UMTS k adresování konkrétní skupiny mobilních stanic (MS) pro skupinové služby, jako je služba hlasových skupinových volání (VGCS) a s"
---

IMGI je jedinečný identifikátor používaný v sítích GSM a UMTS k adresování konkrétní skupiny mobilních stanic (MS) pro skupinové služby, jako je hlasová skupinová volání (VGCS) a hlasové vysílání (VBS).

## Popis

International Mobile Group Identity (IMGI) je strukturovaný identifikátor používaný v okruhově přepínaných mobilních sítích, zejména GSM a UMTS, k definici skupiny účastníků. Jeho hlavní architektonická role je v rámci Group Call Register ([GCR](/mobilnisite/slovnik/gcr/)) a používá jej Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) pro správu skupinových volání. IMGI je tvořen z Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) domovské sítě skupiny, následovaných Group ID, které jedinečně identifikuje konkrétní skupinu v kontextu této sítě. Tato struktura zajišťuje globální jedinečnost.

Provoz skupinového volání využívajícího IMGI je koordinovaný proces. Když uživatel zahájí skupinové volání (např. stisknutím tlačítka push-to-talk), obsluhující MSC přijme informace o volané straně, které obsahují cílové IMGI. MSC následně dotazuje GCR pomocí tohoto IMGI. GCR obsahuje servisní profil skupiny, včetně seznamu členů (nebo oblasti, kde má být volání vysíláno) a parametrů konfigurace volání. Na základě toho MSC a BSC volání nastaví. Ve službě Voice Group Call Service ([VGCS](/mobilnisite/slovnik/vgcs/)) je v buňce zřízen vyhrazený kanál pro přenos hovoru a všichni členové skupiny v této buňce mohou naslouchat a případně postupně hovořit. U služby Voice Broadcast Service ([VBS](/mobilnisite/slovnik/vbs/)) se jedná o jednosměrné vysílání od iniciátora ke všem posluchačům.

Klíčové síťové komponenty zapojené do procesu jsou MSC, které funguje jako kotva řízení volání; BSC, které spravuje rádiové zdroje pro oblast skupinového volání; a GCR, což je centrální databáze pro definice skupin. IMGI je klíč, který tyto prvky spojuje. Umožňuje síti efektivně spravovat rádiové zdroje využitím jednoho downlink kanálu v buňce pro všechny členy skupiny namísto individuálních spojů, což je zásadní pro scénáře jako zásahy složek veřejné bezpečnosti nebo koordinace vozových parků taxi, kde mnoho uživatelů potřebuje současně stejné informace.

## K čemu slouží

IMGI bylo vytvořeno pro podporu efektivních skupinových komunikačních služeb v raných digitálních mobilních sítích, konkrétně k uspokojení potřeb profesionálních komunit a komunit veřejné bezpečnosti. Před jeho zavedením byly mobilní sítě navrženy výhradně pro komunikaci typu jeden-jeden (point-to-point). To bylo neefektivní a nepraktické pro týmy, které potřebovaly okamžitě komunikovat s mnoha členy, jako jsou policisté, hasiči nebo pracovníci technických služeb.

Vyřešilo problém náročných víceúčastnických volání na síťové zdroje. Zřizování individuálních okruhů pro každého člena velké skupiny by spotřebovalo nadměrnou síťovou kapacitu a způsobilo významná zpoždění při sestavování hovoru. Skupinové služby využívající IMGI ([VGCS](/mobilnisite/slovnik/vgcs/)/VBS) umožňují, aby jediná sada síťových zdrojů (kanál pro přenos hovoru v buňce) byla sdílena všemi naslouchajícími členy skupiny v dané geografické oblasti. To napodobuje funkčnost tradičních systémů vysílaček nebo trunkovaných radiostanic, ale na bázi komerční celoplošné mobilní infrastruktury.

Historický kontext je zakotven ve specifikacích GSM Phase 2+, kde byly vyvíjeny služby nad rámec základní telefonie. IMGI poskytlo standardizovaný adresní mechanismus, aby tyto služby fungovaly interoperabilně napříč různými sítěmi a zeměmi. Zatímco jeho význam poklesl s nástupem IP skupinové komunikace, jako je Mission Critical Push-To-Talk (MCPTT) přes LTE a 5G, IMGI představovalo klíčový krok v přizpůsobení mobilních sítí pro skupinovou komunikaci zásadní pro mise a podnikání a stanovilo základní koncepty pro pozdější pokročilejší skupinové systémy.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro skupinu mobilních stanic (MS)
- Struktura zahrnuje MCC, MNC a jedinečné Group ID
- Klíčový identifikátor pro službu hlasových skupinových volání (VGCS) a službu hlasového vysílání (VBS)
- Používá Group Call Register (GCR) k získání členství ve skupině a servisních parametrů
- Umožňuje efektivní využití sdílených rádiových zdrojů pro komunikaci typu jeden-mnoho
- Primárně definováno pro architektury okruhově přepínaných sítí GSM a UMTS

## Související pojmy

- [VGCS – Voice Group Call Service](/mobilnisite/slovnik/vgcs/)
- [VBS – Voice Broadcast Service](/mobilnisite/slovnik/vbs/)
- [GCR – Global Call Reference](/mobilnisite/slovnik/gcr/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [IMGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/imgi/)
