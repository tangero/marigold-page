---
slug: "pumax"
url: "/mobilnisite/slovnik/pumax/"
type: "slovnik"
title: "PUMAX – Configured Maximum UE Output Power"
date: 2025-01-01
abbr: "PUMAX"
fullName: "Configured Maximum UE Output Power"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pumax/"
summary: "PUMAX je měřený nastavený maximální výstupní výkon uživatelského zařízení (UE) definovaný 3GPP. Jde o klíčový parametr pro zajištění dodržování regulačních limitů, řízení síťové interference a optimal"
---

PUMAX je nastavený maximální výstupní výkon uživatelského zařízení (UE), klíčový parametr pro zajištění souladu s regulacemi, řízení interference a optimalizaci správy rádiových prostředků v sítích 3GPP.

## Popis

PUMAX, neboli nastavený maximální výstupní výkon UE, je standardizované měření definované ve specifikacích 3GPP, primárně v řadě 38.101 pro NR (New Radio) a souvisejících testovacích specifikacích. Představuje maximální úroveň vysílacího výkonu, kterou je UE nastaveno používat, jak je určeno síťovou signalizací a schopnostmi UE. Tento parametr není statický hardwarový limit, ale dynamicky nastavitelné horní omezení stanovené sítí na základě faktorů, jako je provozní pásmo, kmitočtový rozsah, výkonová třída UE a regulační požadavky. Síť tuto hranici sděluje prostřednictvím signalizace řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a UE se jí musí při vysílání v uplinku řídit, aby bylo zajištěno efektivní využití spektra a soulad.

Z architektonického hlediska je PUMAX řízen ve fyzické vrstvě a vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) UE. gNodeB (gNB) v rádiové přístupové síti (RAN) určuje vhodnou hodnotu PUMAX na základě hlášené rezervy výkonu UE, stavu kanálu a celkového zatížení sítě. Tato hodnota je následně předána UE prostřednictvím vyhrazených RRC zpráv, jako je zpráva RRCReconfiguration, která obsahuje parametry jako P-Max. Výkonové řídicí algoritmy UE používají PUMAX jako strop, upravují skutečný vysílací výkon pro konkrétní kanály (např. [PUSCH](/mobilnisite/slovnik/pusch/), [PUCCH](/mobilnisite/slovnik/pucch/), [SRS](/mobilnisite/slovnik/srs/)) na základě odhadů útlumu na trase a příkazů výkonového řízení, ale nikdy nepřekračují PUMAX.

Role PUMAX v síti je mnohostranná. Primárně zajišťuje, aby UE nevysílala na výkonových úrovních, které by mohly způsobit nadměrnou interferenci sousedním buňkám nebo porušit regulační masky spektrální emise. To je klíčové pro udržení celkové kapacity sítě a kvality služeb, zejména v hustých nasazeních. PUMAX navíc pomáhá řídit spotřebu baterie UE tím, že brání zbytečným vysíláním na vysoký výkon. V testovacích a konformačních scénářích, jak je popsáno ve specifikacích jako 38.521-1, se PUMAX měří, aby se ověřilo, že UE splňují stanovené požadavky na přesnost výstupního výkonu a úrovně tolerance, což zajišťuje interoperabilitu a spolehlivý výkon napříč zařízeními různých výrobců.

## K čemu slouží

PUMAX byl zaveden, aby řešil potřebu přesné kontroly vysílacího výkonu UE v sítích 5G NR, navazující na podobné koncepty v LTE, ale s rozšířenými požadavky pro širší kmitočtové rozsahy a různorodé scénáře nasazení. U dřívějších generací mobilních sítí se výkonové řízení primárně zaměřovalo na dynamické úpravy pro adaptaci spoje, ale jak se sítě vyvíjely s agregací nosných, massive [MIMO](/mobilnisite/slovnik/mimo/) a milimetrovými vlnami, význam nastavitelného maximálního výkonového limitu se stal výraznějším. To umožňuje síti dynamicky optimalizovat správu rádiových prostředků namísto spoléhání se pouze na statické definice výkonových tříd UE.

Zavedení PUMAX bylo motivováno několika technickými výzvami. Za prvé, 5G NR funguje v širokém spektru od pásem pod 1 GHz až po milimetrové vlny, z nichž každé má odlišné charakteristiky šíření a regulační omezení. Univerzální přístup s jedním maximálním výkonem je nedostatečný; PUMAX umožňuje konfiguraci specifickou pro síť podle pásma a scénáře. Za druhé, ve scénářích jako síťové segmentování nebo ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) je přesné výkonové řízení zásadní pro splnění přísných požadavků na QoS bez způsobení interference. PUMAX poskytuje nastavitelné horní omezení, které síť může upravovat na základě podmínek v reálném čase, čímž zlepšuje spektrální účinnost a koexistenci s dalšími rádiovými systémy.

PUMAX dále řeší omezení předchozích přístupů, kde byl maximální výkon z velké části pevně dán hardwarovými schopnostmi UE nebo byl volně definován. Tím, že se z něj stal konfigurovatelný parametr, standardy 3GPP usnadňují flexibilnější síťové operace, podporu pokročilých funkcí, jako je sdílení výkonu v uplinku při agregaci nosných, a lepší soulad s globálními regulačními rámci. To zajišťuje, že sítě 5G mohou poskytovat konzistentní výkon při dodržování přísných emisních standardů, což nakonec zlepšuje uživatelský zážitek a spolehlivost sítě.

## Klíčové vlastnosti

- Dynamicky konfigurovatelný prostřednictvím RRC signalizace
- Zajišťuje soulad s regulačními výkonovými limity
- Podporuje výkonové řízení napříč více kmitočtovými rozsahy NR
- Integruje se s hlášením rezervy výkonu UE
- Používá se v konformačním testování dle specifikací 3GPP
- Zlepšuje řízení interference a kapacitu sítě

## Související pojmy

- [SAR – Security Assurance Requirements](/mobilnisite/slovnik/sar/)

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.887** (Rel-16) — NR Band n259 Specification (39.5-43.5 GHz)

---

📖 **Anglický originál a plná specifikace:** [PUMAX na 3GPP Explorer](https://3gpp-explorer.com/glossary/pumax/)
