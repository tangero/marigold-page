---
slug: "mich"
url: "/mobilnisite/slovnik/mich/"
type: "slovnik"
title: "MICH – MBMS notification Indicator Channel"
date: 2025-01-01
abbr: "MICH"
fullName: "MBMS notification Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mich/"
summary: "Downlinkový fyzický kanál v UMTS, který přenáší oznamovací indikátory pro relace služby Multimedia Broadcast Multicast Service (MBMS). Upozorňuje uživatelské zařízení (UE) na nadcházející MBMS přenosy"
---

MICH je downlinkový fyzický kanál v UMTS, který přenáší oznamovací indikátory, aby upozornil uživatelské zařízení na nadcházející přenosy služby Multimedia Broadcast Multicast Service.

## Popis

Kanál [MBMS](/mobilnisite/slovnik/mbms/) notification Indicator Channel (MICH) je vyhrazený fyzický kanál v systému Universal Mobile Telecommunications System (UMTS), speciálně navržený pro podporu služby Multimedia Broadcast Multicast Service (MBMS). Funguje ve směru downlink, z NodeB k uživatelskému zařízení (UE), a je přenášen přes rozhraní vzduchu pomocí technologie WCDMA. MICH přenáší oznamovací indikátory, což jsou krátké signalizační zprávy informující UE o bezprostředním zahájení nebo změně MBMS relací. Tyto indikátory jsou namapovány na specifický bitový vzor na kanálu, což umožňuje UE rychle je dekódovat s minimální spotřebou energie. MICH je typicky asociován se Secondary Common Control Physical Channel (S-CCPCH) a používá pevný spreading faktor pro zajištění spolehlivého příjmu v celé buňce.

Při provozu MICH spolupracuje s dalšími MBMS kanály, jako je MBMS Point-to-Multipoint Control Channel ([MCCH](/mobilnisite/slovnik/mcch/)) a MBMS Traffic Channel ([MTCH](/mobilnisite/slovnik/mtch/)). Když síť zahájí MBMS službu (např. mobilní TV nebo aktualizace softwaru), Radio Network Controller (RNC) nakonfiguruje MICH pro vysílání oznamovacích indikátorů. Tyto indikátory jsou periodicky vysílány a UE nakonfigurovaná pro MBMS je nepřetržitě monitorují v idle nebo connected stavech. Po detekci relevantního indikátoru UE ví, že se má probudit a přijmout podrobné informace o relaci z MCCH, které následně naplánuje přenos dat na MTCH. Tento dvoukrokový proces snižuje vybíjení baterie UE tím, že se vyhne neustálému monitorování kanálů vyšších vrstev.

Klíčové součásti MICH zahrnují bity oznamovacích indikátorů, které jsou kódovány a modulovány pomocí QPSK, a kanalizační kód, který odlišuje MICH od ostatních fyzických kanálů. Kanál je charakterizován svým časováním, přičemž přenosové časové intervaly (TTI) jsou synchronizovány s dynamikou MBMS relací. MICH podporuje více oznamovacích skupin, což umožňuje upozorňovat různá UE na různé služby na základě předplatného nebo zájmu. Jeho návrh upřednostňuje nízkou složitost a vysoké pokrytí, což zajišťuje, že i UE na okraji buňky mohou oznámení spolehlivě přijímat. V architektuře UMTS je MICH spravován RNC prostřednictvím signalizace [NBAP](/mobilnisite/slovnik/nbap/) k NodeB, čímž se integruje do širšího MBMS rámce definovaného v 3GPP Release 6.

Role MICH je klíčová pro efektivitu MBMS, protože umožňuje UE přecházet do spánkových režimů, když nejsou aktivní žádné služby, a tím prodlužuje výdrž baterie. Také optimalizuje síťové zdroje snížením zbytečné signalizační režie. Kanál funguje v režimu [FDD](/mobilnisite/slovnik/fdd/) a je součástí specifikací fyzické vrstvy v TS 25.211, které detailně popisují jeho rámcovou strukturu a mapování na rádiové rámce. MICH je příkladem inovací fyzické vrstvy v UMTS pro podporu broadcast/multicast služeb, které vyvažují výkon s omezeními spotřeby energie UE. Jak se MBMS vyvinulo v eMBMS v LTE, podobné oznamovací mechanismy byly integrovány do [MCH](/mobilnisite/slovnik/mch/) Scheduling Information ([MSI](/mobilnisite/slovnik/msi/)) na MCCH, ale MICH zůstává základním konceptem pro 3G multicast.

## K čemu slouží

MICH byl vytvořen, aby řešil výzvu efektivního oznamování služeb v [MBMS](/mobilnisite/slovnik/mbms/), zavedeném v 3GPP Release 6. Před MBMS byly broadcastové služby v mobilních sítích omezené nebo spoléhaly na point-to-point streaming, což spotřebovávalo nadměrné síťové zdroje a energii UE. Nebyl zde žádný vyhrazený mechanismus pro upozorňování UE na broadcastové relace, což nutilo UE nepřetržitě monitorovat řídicí kanály a vedlo k rychlému vybíjení baterie. MICH to vyřešil poskytnutím nízkopříkonového kanálu na fyzické vrstvě speciálně pro oznámení, což umožnilo UE spát a probouzet se pouze v případě potřeby.

Primární problém, který MICH řeší, je optimalizace spotřeby energie UE během MBMS relací. Bez MICH by UE musela často dekódovat řídicí kanály vyšších vrstev (jako MCCH), aby zkontrolovala dostupnost služeb, což zvyšuje zatížení zpracování a spotřebu energie. Jednoduchá struktura indikátorů MICH umožňuje rychlé dekódování s minimální aktivací hardwaru, což je klíčové pro mobilní zařízení. Také snižuje zahlcení sítě minimalizací zbytečné aktivity UE, protože pouze zainteresovaná UE reagují na oznámení. To bylo motivováno rostoucí poptávkou po multimediálních broadcastových službách, jako je živé TV nebo skupinová komunikace, kde byla klíčová efektivní škálovatelnost.

Historicky byl vývoj MICH hnán potřebou učinit MBMS komerčně životaschopným pro operátory a uživatele. Řešil omezení dřívějších oznamovacích metod v 2G nebo pre-Release 6 UMTS, které nebyly navrženy pro multicast. Integrací do fyzické vrstvy MICH zajistil včasná a spolehlivá upozornění i v nepříznivých rádiových podmínkách. Jeho vytvoření podpořilo cíl 3GPP vylepšit broadcastové schopnosti a připravilo cestu pro pozdější vylepšení v LTE eMBMS a 5G broadcastu.

## Klíčové vlastnosti

- Downlinkový fyzický kanál v UMTS používající technologii WCDMA pro MBMS oznámení
- Přenáší oznamovací indikátory pro upozornění UE na nadcházející zahájení nebo změny MBMS relace
- Umožňuje úsporu energie UE tím, že povoluje nespojitý příjem (DRX) řídicích kanálů
- Funguje s pevným spreading faktorem a modulací QPSK pro spolehlivé pokrytí
- Integruje se do MBMS architektury prostřednictvím konfigurace RNC a asociace se S-CCPCH
- Podporuje více oznamovacích skupin pro diferencovaná upozornění na služby

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [MICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mich/)
