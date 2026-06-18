---
slug: "svc"
url: "/mobilnisite/slovnik/svc/"
type: "slovnik"
title: "SVC – Switched Virtual Circuit"
date: 2025-01-01
abbr: "SVC"
fullName: "Switched Virtual Circuit"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/svc/"
summary: "Switched Virtual Circuit (SVC, komutovaný virtuální okruh) je spojově orientované spojení dynamicky zřizované na požadavek po dobu trvání komunikační relace, používané v legacy sítích 2G/3G GSM a UMTS"
---

SVC (komutované virtuální okruhy) je spojově orientované spojení dynamicky zřizované na požadavek pro danou relaci, které poskytuje vyhrazenou cestu se zaručenou šířkou pásma v legacy sítích 2G/3G pro hlasové a datové služby.

## Popis

Switched Virtual Circuit (SVC, komutovaný virtuální okruh) je typ spojově orientovaného spojení používaného v tradičních telekomunikačních sítích, včetně systémů GSM a UMTS standardizovaných 3GPP. Na rozdíl od trvalé fyzické pronajaté linky je SVC dynamicky zřizován signalizačními procedurami při zahájení hovoru a ukončen po skončení hovoru. V kontextu 3GPP odkazuje na koncové spojení zřízené pro Circuit-Switched ([CS](/mobilnisite/slovnik/cs/)) hovor, které prochází více síťovými elementy. Cesta je „virtuální“, protože může sdílet fyzické přenosové prostředky (jako časové sloty na lince E1) s jinými okruhy, ale logicky je vyhrazena pro jeden hovor po dobu jeho trvání, což poskytuje zaručenou a konzistentní šířku pásma.

Architektura pro SVC v GSM/UMTS zahrnuje mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), subsystém základnových stanic ([BSS](/mobilnisite/slovnik/bss/)), ústřednu mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) a případně bránovou MSC ([GMSC](/mobilnisite/slovnik/gmsc/)). Klíčovým protokolem pro zřízení SVC je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo jeho mobilní varianta Bearer Independent Call Control (BICC), používaná mezi MSC a směrem k [PSTN](/mobilnisite/slovnik/pstn/). V rámci rádiové přístupové sítě je přidělen kanál pro přenos uživatelských dat (TCH) a v rámci jádra sítě jsou časové sloty na PCM linkách (rozhraní A, rozhraní E) vzájemně propojeny, aby vytvořily úplný okruh. Signalizace řízení hovoru (prostřednictvím protokolů jako DTAP a BSSAP) zřizuje SVC rezervací těchto prostředků podél vypočtené cesty předtím, než začne proudit konverzační média.

Fungování začíná požadavkem na zřízení hovoru. Výchozí MSC analyzuje volané číslo, směruje hovor a používá signalizaci ISUP k rezervaci po sobě jdoucích časových slotů na každé trunkové lince k další ústředně, až dosáhne cílové MSC. Každá ústředna na cestě nakonfiguruje svůj přepojovací prvek tak, aby propojila příchozí časový slot s odchozím časovým slotem pro tento konkrétní hovor. Tím vznikne souvislá, synchronní digitální cesta o rychlosti 64 kbps (nebo její násobek pro datové služby jako HSCSD). Tento proces zajišťuje nízké a konstantní zpoždění, které bylo ideální pro hlas v reálném čase. SVC zůstává aktivní a spotřebovává síťové prostředky, dokud signalizační sekvence pro uvolnění hovoru nezpůsobí, že každá ústředna zruší přepojení a vrátí časové sloty do sdíleného fondu.

## K čemu slouží

Technologie Switched Virtual Circuit (SVC, komutovaný virtuální okruh) existovala za účelem poskytování efektivních, na požadavek zřizovaných, vyhrazených spojení pro hlasovou komunikaci v reálném čase v digitálních telefonních sítích, včetně mobilních systémů 2G a 3G. Řešila problém, jak sdílet drahou přenosovou infrastrukturu mezi mnoha uživateli, a přitom poskytovat konzistentní kvalitu a časové charakteristiky fyzického okruhu. Před digitálními SVC měly analogové mobilní systémy omezenou kapacitu a kvalitu.

Historicky byly SVC základním kamenem filozofie Integrated Services Digital Network (ISDN) přijaté GSM. Odstraňovaly omezení trvalých okruhů, které byly nehospodárné pro přerušované hlasové hovory, a paketově orientovaných spojení té doby, která nemohla garantovat nízké zpoždění a chvění (jitter) vyžadované pro hlas služební kvality. Vytvoření modelu SVC v rámci GSM (od R99 dále) umožnilo mobilním sítím bezproblémově spolupracovat s existující globální PSTN, která byla také založena na spojovém přepojování. Umožnilo službu hlasu „kdykoli a kdekobykoli“, která definovala ranou mobilní telefonii.

Motivace byla hnána potřebou spolehlivé, vysoce kvalitní hlasové služby jako primární zásadní aplikace pro mobilní sítě. SVC poskytovaly předvídatelný výkon, zjednodušovaly účtování (na základě doby spojení) a přirozenou migrační cestu z pevné telefonie. Jak je specifikováno v dokumentech 3GPP jako TS 23.107 (QoS) a TS 25.410 (rozhraní UTRAN Iu), byl SVC nositelem pro třídu QoS Conversational. Jeho statická spotřeba prostředků i během období ticha se však stala klíčovým omezením, které nakonec motivovalo přechod na plně IP Voice over IP (VoIP) a IMS v 4G LTE, které používají statisticky multiplexované paketově orientované nosiče.

## Klíčové vlastnosti

- Dynamicky zřizován a uvolňován pro každý hovor
- Poskytuje vyhrazenou cestu se zaručenou šířkou pásma (typicky 64 kbps na časový slot)
- Používá technologii spojového přepojování se synchronním časovým multiplexem (TDM)
- Zřizován prostřednictvím signalizačních protokolů mimo přenosové pásmo, jako jsou ISUP a BICC
- Tvoří nosič pro Circuit-Switched (CS) hlasové a datové služby v 2G/3G
- Zajišťuje nízké, konstantní zpoždění ideální pro služby konverzace v reálném čase

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.903** (Rel-19) — Video Capability Requirements for PSS and MBMS
- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 48.103** (Rel-19) — A Interface User Plane Transport Protocols

---

📖 **Anglický originál a plná specifikace:** [SVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/svc/)
