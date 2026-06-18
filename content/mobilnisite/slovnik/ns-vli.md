---
slug: "ns-vli"
url: "/mobilnisite/slovnik/ns-vli/"
type: "slovnik"
title: "NS-VLI – Network Service Virtual Link Identifier"
date: 2025-01-01
abbr: "NS-VLI"
fullName: "Network Service Virtual Link Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ns-vli/"
summary: "NS-VLI je jedinečný identifikátor pro virtuální spojení síťové služby (Network Service Virtual Link – NS-VL) v rámci řídicího rámce 3GPP. Používá se k rozlišení a správě logických komunikačních cest m"
---

NS-VLI je jedinečný identifikátor pro virtuální spojení síťové služby (Network Service Virtual Link) používaný v rámci řídicího rámce 3GPP k rozlišení a správě logických komunikačních cest mezi síťovými funkcemi.

## Popis

Identifikátor virtuálního spojení síťové služby (Network Service Virtual Link Identifier – NS-VLI) je základním prvkem v modelu síťových zdrojů 3GPP (Network Resource Model – [NRM](/mobilnisite/slovnik/nrm/)) definovaném v TS 48.016. Slouží jako jedinečný klíč pro identifikaci objektu typu virtuální spojení síťové služby (Network Service Virtual Link – [NS-VL](/mobilnisite/slovnik/ns-vl/)). NS-VL představuje logické, virtualizované komunikační propojení nebo službu konektivity mezi dvěma či více síťovými funkcemi (Network Functions – NFs) nebo koncovými body v rámci spravovaného síťového segmentu nebo instance služby. NS-VLI není jen prostá značka; jde o strukturovaný atribut, který síťovému řídicímu systému, jako je funkce správy podsítě síťového segmentu (Network Slice Subnet Management Function – NSSMF) nebo funkce správy síťového segmentu (Network Slice Management Function – [NSMF](/mobilnisite/slovnik/nsmf/)), umožňuje jedinečně odkazovat, konfigurovat, monitorovat a měnit vlastnosti tohoto virtuálního spojení.

Z architektonického hlediska je NS-VLI atributem spravované objektové třídy NS-VL v rámci hierarchie tříd informačních objektů (Information Object Class – [IOC](/mobilnisite/slovnik/ioc/)) modelu NRM. Tento model používají řídicí rozhraní, především rozhraní Itf-N, pro komunikaci mezi systémem podpory provozu (Operation Support System – [OSS](/mobilnisite/slovnik/oss/)) a vrstvou síťového managementu (Network Management – [NM](/mobilnisite/slovnik/nm/)) nebo mezi různými vrstvami NM. Při vytváření instance síťového segmentu nebo komplexní síťové služby orchestrátor vytvoří různé objekty NS-VL, aby definoval požadovanou topologii konektivity mezi virtualizovanými síťovými funkcemi (Virtualized Network Functions – VNFs) a fyzickými síťovými funkcemi (Physical Network Functions – PNFs). Každému z těchto objektů NS-VL je přidělen jedinečný NS-VLI. Tento identifikátor je pak používán ve všech následných řídicích operacích, jako jsou požadavky na monitorování výkonu, upozornění na poruchy nebo aktualizace konfigurace cílené na konkrétní virtuální spojení.

Role NS-VLI je klíčová pro automatizaci a operace v uzavřené smyčce. Umožňuje řídicím systémům korelovat telemetrická data, alarmy a stavy konfigurace s konkrétním logickým spojením v dynamickém, softwarově definovaném prostředí. Například při překročení prahové hodnoty výkonu na spojení přenášejícím provoz specifický pro segment bude vygenerovaný alarm odkazovat na NS-VLI, což řídicímu systému umožní okamžitě identifikovat postiženou komponentu konektivity daného segmentu. Dále, ve scénářích zahrnujících škálování nebo ozdravné akce, se NS-VLI používá k identifikaci spojení, která je třeba překonfigurovat nebo znovu navázat při přidávání, odebírání nebo migraci síťových funkcí. Jeho konzistentní použití v celém řídicím rámci zajišťuje, že logická topologie služby zůstává přesně zmapována a řiditelná po celý její životní cyklus.

## K čemu slouží

NS-VLI byl zaveden, aby řešil složitosti správy vyplývající z virtualizace a softwarizace sítí, zejména s nástupem virtualizace síťových funkcí (Network Function Virtualization – [NFV](/mobilnisite/slovnik/nfv/)) a později síťových segmentů (network slicing). V tradičních, hardwareově orientovaných sítích byly fyzické spoje identifikovatelné pomocí fyzických portů, kabelů a identifikátorů okruhů. Ve virtualizovaném prostředí, kde více logických sítí (segmentů) sdílí stejnou fyzickou infrastrukturu, však vznikla potřeba vytvářet, identifikovat a spravovat logická spojení nezávisle na podkladové fyzické topologii. NS-VLI poskytuje tuto nezbytnou abstrakci.

Před existencí takových identifikátorů byla správa virtuální konektivity často ad-hoc, zabudovaná do skriptů specifických pro službu, nebo přímo vázaná na identifikátory nižších vrstev, jako jsou ID [VLAN](/mobilnisite/slovnik/vlan/) nebo IP tunely, což mísilo logiku služby s detaily přenosu. To činilo správu životního cyklu služby těžkopádnou, náchylnou k chybám a neškálovatelnou pro automatizované, na požádání poskytované služby. Zavedení NS-VLI jako standardizovaného atributu v rámci modelu NRM 3GPP poskytlo řídicím systémům jednotný, technologicky agnostický způsob, jak odkazovat na tato virtuální spojení. Odděluje vrstvu správy služeb a segmentů od implementačních detailů konektivity přenosové roviny, což umožňuje jasné oddělení kompetencí. Tato abstrakce je klíčovým prvkem umožňujícím vizi agilního poskytování služeb a efektivního využití zdrojů v sítích 5G a budoucích generací.

## Klíčové vlastnosti

- Jednoznačná identifikace logických spojovacích cest v rámci spravované služby nebo segmentu.
- Standardizovaný atribut v rámci modelu síťových zdrojů 3GPP (TS 48.016).
- Umožňuje automatizovanou správu životního cyklu (Lifecycle Management – LCM) virtuálních spojení.
- Umožňuje korelaci poruch, dat o výkonu a konfigurace s konkrétními prvky topologie služby.
- Podporuje síťové segmenty (network slicing) poskytováním identifikátorů spojení specifických pro segment.
- Používá se napříč řídicími rozhraními (např. Itf-N) pro konzistentní odkazování.

## Definující specifikace

- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [NS-VLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns-vli/)
