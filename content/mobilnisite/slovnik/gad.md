---
slug: "gad"
url: "/mobilnisite/slovnik/gad/"
type: "slovnik"
title: "GAD – Universal Geographical Area Description"
date: 2025-01-01
abbr: "GAD"
fullName: "Universal Geographical Area Description"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gad/"
summary: "Standardizovaný formát pro popis geografických oblastí v sítích 3GPP. Umožňuje služby založené na poloze tím, že poskytuje společný jazyk pro definování regionů, zón nebo bodů pro síťové aplikace a už"
---

GAD je standardizovaný formát pro popis geografických oblastí v sítích 3GPP, který umožňuje služby založené na poloze tím, že poskytuje společný jazyk pro definování regionů, zón nebo bodů.

## Popis

Universal Geographical Area Description (GAD) je základní koncept ve specifikacích 3GPP, který poskytuje standardizovanou metodu pro popis geografických oblastí. Nejde o jeden konkrétní protokol, ale o sadu definic a kódování používaných napříč různými síťovými rozhraními a aplikacemi. GAD definuje, jak jsou strukturovány a komunikovány geografické informace – jako body, elipsoidní body, polygony a elipsoidní oblouky. Tento strukturovaný popis umožňuje síťovým entitám a uživatelským zařízením (UE) jednoznačně interpretovat data související s polohou.

Architektura GAD je integrována do širšího rámce služeb polohování ([LCS](/mobilnisite/slovnik/lcs/)) v 3GPP. Používá se v signalizačních zprávách mezi uzly jádra sítě, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) a Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)), stejně jako v protokolech jako Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) a Diameter. Formát GAD zahrnuje parametry pro tvar, souřadnice a nejistotu, což umožňuje přesné nebo přibližné definice oblastí v závislosti na požadavcích služby. Například může popsat oblast pokrytí buňky, předdefinovanou geofence nebo cílovou oblast pro výstrahy založené na poloze.

Klíčové součásti GAD zahrnují typ tvaru (např. elipsoidní bod, polygon), geografické souřadnice (obvykle používající World Geodetic System 1984, WGS84) a přidružené úrovně nejistoty nebo spolehlivosti. Tyto součásti jsou kódovány podle pravidel ASN.1 specifikovaných v technických specifikacích 3GPP. Role GAD je klíčová pro umožnění služeb, jako je lokalizace volajícího v nouzových případech, účtování založené na poloze, správa vozových parků a vylepšená služba 911 (E911). Poskytnutím univerzálního formátu zajišťuje interoperabilitu mezi různými síťovými prvky a napříč různými generacemi mobilních sítí od GSM po 5G.

## K čemu slouží

GAD byl vytvořen, aby vyřešil problém nekonzistentních a proprietárních geografických popisů v raných mobilních sítích. Před standardizací používali výrobci a operátoři ad-hoc metody pro definování oblastí, což vedlo k problémům s interoperabilitou a brzdilo zavádění služeb založených na poloze. Potřeba univerzálního formátu se stala naléhavou s regulatorními požadavky na nouzové služby (např. E112 v Evropě) a komerčním potenciálem aplikací využívajících polohu.

Historický kontext spočívá ve vývoji ze sítí GSM do 3G, kde se služby polohování staly povinnou funkcí. GAD, zavedený ve vydání 4, poskytl společný jazyk, který umožnil síťovým zařízením od různých výrobců bezproblémově si vyměňovat geografické informace. Řešil omezení, jako byla neschopnost přesně definovat složité geografické zóny nebo vyjádřit nejistotu v odhadech polohy. Standardizací popisu GAD umožnil vývoj široké škály služeb, které spoléhají na přesné a interpretovatelné definice oblastí, od navigačních pomůcek po geofencing pro zařízení IoT.

## Klíčové vlastnosti

- Standardizované kódování pro geografické tvary (bod, elipsa, polygon, oblouk)
- Používá souřadnicový referenční systém WGS84 pro globální konzistenci
- Zahrnuje parametry nejistoty a spolehlivosti pro přesnost polohy
- Integrováno do více protokolů 3GPP (MAP, Diameter) pro širokou použitelnost
- Podporuje jak 2D, tak 3D geografické popisy
- Umožňuje interoperabilitu napříč různými generacemi sítí a zařízeními různých výrobců

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 23.032** (Rel-19) — Universal Geographical Area Description
- **TS 24.080** (Rel-19) — Mobile radio interface layer 3 supplementary services
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2

---

📖 **Anglický originál a plná specifikace:** [GAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/gad/)
