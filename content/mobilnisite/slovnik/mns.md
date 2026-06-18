---
slug: "mns"
url: "/mobilnisite/slovnik/mns/"
type: "slovnik"
title: "MNS – Mobile Network Signalling"
date: 2025-01-01
abbr: "MNS"
fullName: "Mobile Network Signalling"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mns/"
summary: "Základní protokolová vrstva v architektuře 3GPP, která přenáší signalizaci řídicí roviny pro spojově orientované (CS) mobilní služby. Funguje jako síťová vrstva (vrstva 3) v zásobníku protokolů řídicí"
---

MNS je protokol síťové vrstvy 3GPP zodpovědný za navazování, udržování a uvolňování spojově orientovaných (circuit-switched) spojení, například pro hlasové hovory a SMS, v mobilních sítích 2G a 3G.

## Popis

Mobile Network Signalling (MNS) je klíčový protokol definovaný v 3GPP TS 24.007. Nachází se na síťové vrstvě (vrstva 3) zásobníku protokolů řídicí roviny pro spojově orientovanou ([CS](/mobilnisite/slovnik/cs/)) komunikaci mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a sítí. MNS je postaven na vrstvě datového spoje (vrstva 2), konkrétně na protokolu LAPDm na rádiovém rozhraní. Jeho hlavní funkcí je poskytovat signalizační procedury pro řízení spojení, správu mobility a řízení hovorů pro tradiční hlasové a doplňkové služby.

MNS funguje prostřednictvím výměny specifických zpráv mezi MS a Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)). Je rozdělen do několika podvrstev neboli entit, nejvýznamněji podvrstvy Connection Management ([CM](/mobilnisite/slovnik/cm/)) a Mobility Management ([MM](/mobilnisite/slovnik/mm/)). Podvrstva MM zajišťuje funkce jako aktualizace polohy, autentizace a navázání zabezpečeného signalizačního spojení. Jakmile je MM spojení navázáno, podvrstva CM spravuje vlastní procedury související se službami, které zahrnují Call Control ([CC](/mobilnisite/slovnik/cc/)) pro sestavování a ukončování hlasových hovorů, správu doplňkových služeb ([SS](/mobilnisite/slovnik/ss/)) a podporu služby krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)).

Protokol pracuje na principu stavových automatů. Jak MS, tak síť udržují stavy (např. IDLE, MM-CONNECTED) a přecházejí mezi nimi na základě přijatých zpráv a interních podnětů. Například pro zahájení hovoru odešle entita CM v MS zprávu SETUP přes navázané MM spojení. Protokol MNS zajišťuje, že tyto zprávy jsou správně formátovány, řazeny a interpretovány. Ačkoli je MNS silně spojován se sítí 2G GSM, jeho principy a zprávy byly přeneseny do CS domény sítě 3G UMTS, kde fungoval nad protokolem Radio Resource Control (RRC). Jeho návrh je klíčový pro spolehlivost a interoperabilitu základních služeb mobilní telefonie.

## K čemu slouží

MNS byl vytvořen, aby poskytoval standardizovaný, robustní signalizační systém pro první digitální celulární sítě (GSM). Před GSM měly analogové systémy omezenou a často proprietární signalizaci, což bránilo interoperabilitě a vývoji pokročilých služeb. Vytvoření MNS bylo motivováno potřebou jednotného protokolu pro zvládnutí složitých úkolů mobility (sledování uživatele napříč buňkami a oblastmi polohy), zabezpečeného přístupu (autentizace a šifrování) a spolehlivého sestavování hovorů v čistě spojově orientovaném prostředí.

Řešil problém, jak spravovat stav a služby mobilního účastníka nezávisle na podkladovém rádiovém přenosu. Oddělením signalizace (řídicí rovina) od vlastního hlasového provozu (uživatelská rovina) umožnil MNS efektivní využití rádiových zdrojů a zavedení sofistikovaných funkcí, jako je mezinárodní roaming, přesměrování hovorů a SMS. Jako základ úspěchu GSM stanovil MNS architektonický vzor vrstvené signalizace řídicí roviny, který pokračoval i v pozdějších systémech 3GPP, a to i když se jádrová síť vyvíjela směrem k dominanci paketového přenosu s IMS a VoLTE.

## Klíčové vlastnosti

- Poskytuje signalizaci vrstvy 3 (síťová vrstva) pro spojově orientovanou (CS) doménu
- Zahrnuje klíčové podvrstvy: Mobility Management (MM) a Connection Management (CM)
- Spravuje kritické procedury, jako je aktualizace polohy, autentizace a sestavování hovorů
- Definuje sadu zpráv a stavové automaty pro řízení CS služeb
- Funguje nad vrstvami datového spoje LAPDm (GSM) nebo RRC (UMTS)
- Základní pro základní hlasové služby, SMS a doplňkové služby v sítích 2G/3G

## Související pojmy

- [MM – Mobility Management](/mobilnisite/slovnik/mm/)
- [CM – Configuration Management](/mobilnisite/slovnik/cm/)
- [DTAP – Direct Transfer Application Part](/mobilnisite/slovnik/dtap/)

## Definující specifikace

- **TS 24.007** (Rel-19) — GSM Um Interface Layer 3 Architecture

---

📖 **Anglický originál a plná specifikace:** [MNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mns/)
