---
slug: "guami"
url: "/mobilnisite/slovnik/guami/"
type: "slovnik"
title: "GUAMI – Globally Unique AMF Identifier"
date: 2026-01-01
abbr: "GUAMI"
fullName: "Globally Unique AMF Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/guami/"
summary: "Globálně jednoznačný identifikátor AMF (GUAMI) je klíčový identifikátor v 5G sítích, který jednoznačně identifikuje instanci funkce pro správu přístupu a mobility (AMF) v globálním měřítku. Používá se"
---

GUAMI je globálně jednoznačný identifikátor instance AMF v 5G, používaný ke správnému směrování signalizačních zpráv pro procedury, jako je registrace a předání spojení (handover).

## Popis

Globálně jednoznačný identifikátor [AMF](/mobilnisite/slovnik/amf/) (GUAMI) je strukturovaný identifikátor definovaný v 3GPP pro 5G systém (5GS), který poskytuje globálně jednoznačný způsob identifikace konkrétní instance funkce pro správu přístupu a mobility (AMF). AMF je funkce jádra sítě zodpovědná za ukončení signalizace [NAS](/mobilnisite/slovnik/nas/), správu registrace, správu spojení, správu dosažitelnosti a správu mobility uživatelského zařízení (UE). GUAMI je tvořen ze tří složek: identifikátoru veřejné pozemní mobilní sítě (PLMN) ([MCC](/mobilnisite/slovnik/mcc/) a [MNC](/mobilnisite/slovnik/mnc/)), AMF Region ID, AMF Set ID a AMF Pointer. Tato hierarchická struktura umožňuje efektivní směrování a škálovatelnost uvnitř i napříč PLMN sítěmi.

Z architektonického hlediska je GUAMI přiřazen každé instanci AMF operátorem sítě a je nakonfigurován v rámci operačních parametrů AMF. AMF jej inzeruje ostatním síťovým funkcím, jako jsou uzly rádiového přístupového sítě (RAN) (gNB) přes rozhraní [N2](/mobilnisite/slovnik/n2/) a dalším funkcím jádra, například funkci pro výběr síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)) přes rozhraní služebního typu. Když UE zahájí registraci do 5G sítě, uzel RAN použije GUAMI, často odvozený z dočasné identity mobilního účastníka ([5G-S-TMSI](/mobilnisite/slovnik/5g-s-tmsi/)) nebo poskytnutý v počáteční NAS zprávě, k výběru vhodné AMF pro žádost UE. GUAMI umožňuje RAN směrovat počáteční zprávu UE ke správné instanci AMF, a to i v nasazeních s více AMF pro vyrovnávání zátěže a redundanci.

Provozně hraje GUAMI klíčovou roli v několika procedurách. Během registrace, pokud UE poskytne GUAMI z předchozí registrace (v rámci [5G-GUTI](/mobilnisite/slovnik/5g-guti/)), může jej síť použít k efektivnímu získání kontextu UE. V mobilních scénářích, jako jsou předání spojení (handovery), zdrojová AMF zahrne své GUAMI do žádosti o předání cíli, čímž zajistí, že cílový systém dokáže identifikovat správnou AMF a komunikovat s ní. Při vyhledávání (pagingu) RAN použije GUAMI k určení, na kterou AMF se obrátit, když síť potřebuje kontaktovat nečinné UE. Hierarchická povaha GUAMI (Region ID, Set ID, Pointer) umožňuje operátorům organizovat AMF do logických skupin (Setů) v rámci geografických regionů, což usnadňuje flexibilní nasazení, zotavení po výpadku a efektivní směrování. GUAMI je základním prvkem, který podporuje bezstavovou a službami orientovanou architekturu 5GC a umožňuje dynamické zjišťování a výběr instancí AMF.

## K čemu slouží

GUAMI byl vytvořen, aby řešil výzvy škálovatelnosti, flexibility a směrování, které jsou vlastní službami orientované architektuře 5G jádra (5GC), která odděluje softwarové instance od hardwaru a umožňuje dynamické škálování síťových funkcí. V předchozích generacích, jako je 4G EPS, byla MME identifikována kódem MME a skupinovým ID v rámci PLMN, ale to postrádalo globálně jednoznačný rozsah a granularitu potřebnou pro cloud-nativní, distribuovaná nasazení. Motivací pro GUAMI byla potřeba jednoznačně identifikovat potenciálně tisíce instancí AMF nasazených napříč více datovými centry a geografickými regiony, což podporuje požadavky na síťové řezy (network slicing), edge computing a vysokou dostupnost.

Historicky se identifikátory v mobilních sítích vyvíjely od jednoduchých kódů ke strukturovanějším formám, aby podporovaly rostoucí složitost sítě. Zavedení 5G a jeho požadavek na síťové řezy – kde jedna fyzická síť hostuje více logických sítí – si vyžádalo identifikátor, který by nejen jednoznačně ukazoval na instanci AMF, ale také přenášel informace o logickém seskupení pro efektivní směrování s ohledem na řezy. GUAMI to řeší tím, že zahrnuje PLMN ID, Region ID, Set ID a Pointer, což operátorům umožňuje organizovat AMF způsobem, který odráží topologii jejich nasazení a přidružení k řezům.

Tato technologie řeší kritické problémy v provozu 5G: umožňuje RAN provádět efektivní výběr AMF bez nutnosti centrálního adresáře pro každý požadavek UE, čímž snižuje signalizační latenci. Podporuje bezstavový provoz, kdy instance AMF může selhat a jiná ji může převzít, protože GUAMI poskytuje konzistentní údaj pro lokalizaci kontextu UE. Dále usnadňuje mobilitu a roaming mezi PLMN sítěmi tím, že zajišťuje globální adresovatelnost AMF. Poskytnutím strukturovaného, globálně jednoznačného identifikátoru je GUAMI základním kamenem pro dosažení vize 5G o flexibilní, škálovatelné a odolné jádrové síti, která může podporovat rozmanité služby od hromadného IoT po ultra-spolehlivou komunikaci s nízkou latencí.

## Klíčové vlastnosti

- Globálně jednoznačná identifikace instance AMF napříč všemi PLMN sítěmi
- Hierarchická struktura zahrnující PLMN ID, AMF Region ID, AMF Set ID a AMF Pointer
- Umožňuje efektivní výběr AMF založený na RAN během počáteční registrace UE
- Podporuje bezstavové operace AMF a mechanismy obnovy po výpadku
- Usnadňuje směrování v procedurách mobility, jako je předání spojení (handover) a vyhledávání (paging)
- Nedílná součást síťových řezů (network slicing) pro identifikaci a výběr AMF specifický pro daný řez

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [5G-GUTI – 5G Globally Unique Temporary Identifier](/mobilnisite/slovnik/5g-guti/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.571** (Rel-19) — Common Data Types for 5G Service Based Interfaces
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [GUAMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/guami/)
