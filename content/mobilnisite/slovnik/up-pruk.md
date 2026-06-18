---
slug: "up-pruk"
url: "/mobilnisite/slovnik/up-pruk/"
type: "slovnik"
title: "UP-PRUK – User Plane ProSe Remote User Key"
date: 2025-01-01
abbr: "UP-PRUK"
fullName: "User Plane ProSe Remote User Key"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/up-pruk/"
summary: "Bezpečnostní klíč používaný v 5G ProSe (služby založené na blízkosti) pro přímou komunikaci mezi zařízeními. Zabezpečuje data uživatelské roviny vyměňovaná přes referenční bod PC5 a zajišťuje jejich d"
---

UP-PRUK je bezpečnostní klíč používaný v 5G ProSe k zajištění důvěrnosti a integrity dat uživatelské roviny vyměňovaných přímo mezi zařízeními přes referenční bod PC5.

## Popis

User Plane [ProSe](/mobilnisite/slovnik/prose/) Remote User Key (UP-PRUK, klíč vzdáleného uživatele pro uživatelskou rovinu ProSe) je kryptografický klíč definovaný v bezpečnostní architektuře 3GPP pro služby založené na blízkosti (ProSe), konkrétně pro zabezpečení přímé komunikace mezi uživatelskými zařízeními (UE) přes rozhraní PC5. Tento klíč je klíčový pro zabezpečení uživatelské roviny v přímé komunikaci ProSe, kde zařízení vyměňují aplikační data přímo (např. ve scénářích [V2X](/mobilnisite/slovnik/v2x/) nebo veřejné bezpečnosti) bez směrování přes síťovou infrastrukturu. UP-PRUK je odvozen jako součást hierarchie klíčů zavedené během autorizačních a klíčových managementových procedur přímé komunikace ProSe.

Generování UP-PRUK zahrnuje funkci správy klíčů ProSe (PKMF) v síti. Proces typicky začíná dlouhodobým klíčem sdíleným mezi UE a jeho domovskou sítí. Pro přímou komunikaci se vzdáleným UE požádá ProSe funkce lokálního UE o potřebné klíče od PKMF. PKMF poté vygeneruje nebo odvodí UP-PRUK spolu s dalšími souvisejícími klíči, jako je ProSe Remote User Key ([PRUK](/mobilnisite/slovnik/pruk/)). UP-PRUK je následně bezpečně poskytnut autorizovanému UE, které má v úmyslu navázat přímé spojení. Je jednoznačně spojen s konkrétním párem komunikujících UE (nebo skupinou pro skupinovou komunikaci) a konkrétní službou.

Při provozu UE používá UP-PRUK ve svém protokolovém zásobníku k odvození potřebných klíčů pro šifrování a ochranu integrity dat uživatelské roviny přenášených přes rozhraní PC5. Tyto relakční klíče používá vrstva bezpečnostního protokolu (pravděpodobně v rámci vrstvy [PDCP](/mobilnisite/slovnik/pdcp/) pro NR PC5) k zašifrování uživatelských dat pro důvěrnost a k aplikaci ochrany integrity pro zabránění neoprávněným změnám. Použití vyhrazeného klíče pro uživatelskou rovinu odděluje bezpečnostní aspekty a umožňuje nezávislý management klíčů od zabezpečení signalizace řídicí roviny spoje PC5. Životní cyklus UP-PRUK je spravován sítí; má přidružené podmínky platnosti (jako časové razítko nebo limit použití) a může být podle potřeby PKMF obnoven nebo zneplatněn, což poskytuje robustní správu zabezpečení pro dynamické scénáře přímé komunikace.

## K čemu slouží

UP-PRUK byl vytvořen, aby řešil kritické bezpečnostní požadavky přímé komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)) zavedené a rozšířené ve standardech 3GPP, zejména pro 5G [ProSe](/mobilnisite/slovnik/prose/) a [V2X](/mobilnisite/slovnik/v2x/). Tradiční zabezpečení v buňkových sítích spoléhá na model důvěry mezi UE a sítí, ale přímá komunikace přes PC5 obchází síťovou infrastrukturu a vytváří nový útočný povrch. UP-PRUK řeší problém, jak zabezpečit vlastní uživatelská data (např. senzorová data, bezpečnostní zprávy, obsah chatu) proudící přímo mezi zařízeními, a zajistit tak jejich důvěrnost a nezměněnost i bez nepřetržitého pokrytí sítí.

Jeho zavedení ve vydání Release 17 bylo motivováno vývojem ProSe směrem k pokročilejším a citlivějším případům užití, včetně pokročilých V2X aplikací a komunikací pro veřejnou bezpečnost, které vyžadují robustní, standardizovaný a škálovatelný bezpečnostní mechanismus. Předchozí přístupy v dřívějších vydáních ProSe měly méně vyspělý nebo komplexní management klíčů pro uživatelskou rovinu. UP-PRUK poskytuje strukturovaný rámec pro odvozování a distribuci klíčů s asistencí sítě, který vyvažuje zabezpečení (klíče jsou odvozeny a spravovány sítí) s povahou komunikace mimo síť (klíče jsou předem poskytnuty pro použití bez okamžitého síťového připojení). To umožňuje důvěryhodnou přímou komunikaci jak v rámci pokrytí sítí, tak mimo něj, což je zásadní pro životně důležité operace V2X a veřejné bezpečnosti.

## Klíčové vlastnosti

- Kryptografický klíč pro zabezpečení dat uživatelské roviny na přímém spoji PC5.
- Odvozen a poskytnut síťovou funkcí správy klíčů ProSe (PKMF).
- Umožňuje ochranu důvěrnosti a integrity pro přímou komunikaci ProSe.
- Jednoznačně vázán na konkrétní pár nebo skupinu UE a na službu.
- Součást hierarchie klíčů oddělené od klíčů ProSe pro řídicí rovinu.
- Podporuje scénáře provozu jak v rámci pokrytí sítí, tak mimo něj (částečně nebo plně).

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [PRUK – ProSe Relay User Key Identity](/mobilnisite/slovnik/pruk/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 29.559** (Rel-19) — 5G PKMF Service Based Interface Stage 3
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G

---

📖 **Anglický originál a plná specifikace:** [UP-PRUK na 3GPP Explorer](https://3gpp-explorer.com/glossary/up-pruk/)
