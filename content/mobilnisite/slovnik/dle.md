---
slug: "dle"
url: "/mobilnisite/slovnik/dle/"
type: "slovnik"
title: "DLE – Destination Local Exchange"
date: 2025-01-01
abbr: "DLE"
fullName: "Destination Local Exchange"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dle/"
summary: "Jádrový síťový prvek v okruhově spínané (CS) telefonii, který směruje hovory do jejich konečné destinace v rámci lokální síťové oblasti. Je klíčovou součástí tradičního směrování hovorů v sítích GSM/U"
---

DLE je síťový prvek jádra sítě v okruhově spínané telefonii, který směruje hovory do jejich konečné destinace v rámci lokální síťové oblasti.

## Popis

Cílová místní ústředna (Destination Local Exchange – DLE) je funkční entita v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně sítě GSM nebo UMTS, konkrétně součást architektury veřejné telefonní sítě (PSTN) nebo sítě [ISDN](/mobilnisite/slovnik/isdn/), jak je definováno standardy 3GPP. Představuje místní telefonní ústřednu obsluhující koncového účastníka. Při směrování mobilního odchozího nebo příchozího hovoru sítí se bránová [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje domovského registračního centra ([HLR](/mobilnisite/slovnik/hlr/)) pro získání směrovacích informací. Tyto informace často odkazují na navštívenou MSC (VMSC), kde je účastník aktuálně registrován. Pro hovory určené pevným účastníkům nebo v určitých směrovacích scénářích je však hovor předán právě DLE, která je zodpovědná za konečné fyzické připojení k účastníkově koncové stanici.

Z architektonického hlediska se DLE nachází na okraji jádra sítě a komunikuje s přístupovou sítí pro pevné linky nebo s MSC pro mobilní hovory, které je třeba dokončit v pevné síti. Provádí funkce přepojování hovorů a signalizace na místní úrovni. Mezi klíčové používané protokoly patří ISDN User Part ([ISUP](/mobilnisite/slovnik/isup/)) pro signalizaci řízení hovorů mezi ústřednami. DLE spravuje účastnické linky, poskytuje tónovou volbu, detekuje stav zvednuté sluchátka a připojuje hovor ke správnému fyzickému portu.

Její role v ekosystému 3GPP, ačkoli je zakořeněna v legacy CS infrastruktuře, byla klíčová pro vzájemné propojení mobilních sítí a pevné telefonie. Zajišťovala bezproblémové dokončování hovorů napříč různými typy sítí. V moderních sítích, s přechodem na čistě IP a Voice over LTE (VoLTE)/Voice over NR (VoNR), je funkční role DLE z velké části převzata prvky jádra IMS (IP Multimedia Subsystem), jako je Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pro interworking s legacy PSTN, ale koncept zůstává relevantní pro pochopení historických cest směrování hovorů a určitých scénářů interoperability.

## K čemu slouží

DLE existovala, aby řešila základní problém dokončení telefonního hovoru na konkrétní, pevnou fyzickou lokalitu (účastnickou linku) v rámci hierarchické struktury telefonní sítě. Před nástupem digitálních mobilních sítí byla telefonie výhradně pevná, organizovaná kolem místních ústředen. Vznik mobilních sítí přinesl výzvu směrování hovorů k uživatelům, kteří nebyli vázáni na fyzický kabel. DLE jako součást stávající infrastruktury PSTN/ISDN poskytovala jasně definovaný ukotvovací bod. Jádro mobilní sítě (GMSC/MSC) mohlo použít standardizovanou signalizaci (jako ISUP) k směrování hovoru na DLE asociovanou s telefonním číslem a spoléhat na pevnou síť při zajištění konečného připojení.

Tento přístup umožnil mobilním sítím využít rozsáhlou, existující globální PSTN pro ukončení hovorů bez nutnosti znovuvytvářet místní přístupovou infrastrukturu. Řešil omezení, kdy by mobilní sítě byly izolovanými ostrovy; potřebovaly standardizované rozhraní ke světové telefonní síti. DLE představovala tento standardizovaný koncový bod v hierarchii pevné sítě. Její specifikace ve standardech 3GPP (jako TS 29.013) zajišťovala interoperabilitu mezi MSC mobilních sítí a různými národními architekturami pevných sítí, které byly často postaveny právě na konceptu místních ústředen.

## Klíčové vlastnosti

- Konečný bod ukončení hovoru pro pevné účastníky v rámci lokální oblasti
- Komunikuje s MSC pomocí signalizace ISUP pro navázání a ukončení hovoru
- Spravuje fyzické účastnické linky a poskytuje základní telefonní služby (tónová volba, vyzvánění)
- Provádí místní přepojovací funkce ve své vymezené oblasti ústředny
- Součást hierarchické směrovací struktury sítí PSTN/ISDN
- Umožňuje vzájemné propojení mezi okruhově spínaným jádrem mobilní sítě a legacy sítěmi pevné telefonie

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TS 29.013** (Rel-19) — MAP-SSAP Interworking for CCBS Service

---

📖 **Anglický originál a plná specifikace:** [DLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dle/)
