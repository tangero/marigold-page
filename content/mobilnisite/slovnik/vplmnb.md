---
slug: "vplmnb"
url: "/mobilnisite/slovnik/vplmnb/"
type: "slovnik"
title: "VPLMNB – Visited Public Land Mobile Network of the B subscriber"
date: 2025-01-01
abbr: "VPLMNB"
fullName: "Visited Public Land Mobile Network of the B subscriber"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vplmnb/"
summary: "VPLMNB identifikuje mobilní síť (PLMN), ve které se volaný účastník (B-účastník) aktuálně nachází v roamingu při doručování hovoru. Je klíčový pro směrování ukončovaných hovorů, účtování roamingu a ap"
---

VPLMNB je veřejná pozemní mobilní síť, ve které se volaný účastník nachází v roamingu při doručování hovoru; používá se pro směrování hovorů, účtování roamingu a služby založené na poloze.

## Popis

VPLMNB je protějškem k [VPLMNA](/mobilnisite/slovnik/vplmna/) a představuje navštívenou veřejnou pozemní mobilní síť, ve které je B-účastník – strana přijímající hovor nebo relaci – registrován v době ukončení hovoru. Tento parametr, definovaný v 3GPP TS 23.018, je dynamicky určován během signalizačního procesu doručování a ukončování hovoru. Při směrování hovoru k roamujícímu účastníkovi může síťový prvek odpovědný za lokalizaci tohoto účastníka (typicky Home Location Register nebo [HLR](/mobilnisite/slovnik/hlr/) a Gateway [MSC](/mobilnisite/slovnik/msc/)) parametr VPLMNB zahrnout nebo určit. Tento identifikátor je pak použit v signalizačních zprávách odeslaných k navštívené MSC ([VMSC](/mobilnisite/slovnik/vmsc/)) obsluhující B-účastníka, aby bylo možné dokončit nastavení hovoru.

Z architektonického hlediska funguje VPLMNB v rámci procedur správy mobility a řízení hovorů pro mobilně ukončované hovory. Proces začíná, když Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) dotazuje HLR na informace pro směrování (např. Mobile Station Roaming Number nebo [MSRN](/mobilnisite/slovnik/msrn/)). HLR, který zná aktuální obsluhující síť B-účastníka z adresy [VLR](/mobilnisite/slovnik/vlr/) (Visitor Location Register), může poskytnout nebo implikovat VPLMNB. Tato informace je propagována signalizační cestou. V jádrové síti je přenášena v podobných protokolech jako VPLMNA, například [ISUP](/mobilnisite/slovnik/isup/)/BICC nebo SIP, a poskytuje všem zapojeným uzlům kontext o síti, ve které je hovor ukončován.

Role VPLMNB je mnohostranná. Primárně zajišťuje, že je hovor správně směrován k přesné MSC obsluhující roamujícího účastníka. Je také zásadní pro generování přesných záznamů o účtování na ukončující straně, což umožňuje navštívenému síťovému operátorovi účtovat domácímu operátorovi za využití svých rádiových a jádrových zdrojů k dokončení hovoru (terminační přístupový poplatek). Dále umožňuje specifické zacházení se službami pro volanou stranu na základě jejího stavu roamingu. Například mohou být použita různá pravidla pro přesměrování hovoru nebo tónové oznámení, pokud se účastník nachází v roamingu v konkrétní zemi. Parametr funguje ve spojení s Mobile Station Roaming Number (MSRN) a IMSI, aby jednoznačně identifikoval aktuální bod připojení účastníka k síti. Jeho konzistentní použití je základním kamenem spolehlivého globálního doručování hovorů roamujícím uživatelům.

## K čemu slouží

VPLMNB byl vytvořen k řešení symetrického problému, který řeší VPLMNA, ale pro volanou stranu. V raných mobilních sítích vyžadovalo doručení hovoru roamujícímu účastníkovi, aby síť našla aktuální polohu účastníka, ale kontext *ve které cizí síti* se nachází, nebyl vždy explicitně signalizován. To mohlo vést k neefektivitám a komplikacím při účtování za ukončení hovorů roamujícím účastníkům.

Účelem parametru je explicitně identifikovat síť, ve které bude hovor ukončen, což je nezbytné pro několik provozních a komerčních funkcí. Umožňuje operátorovi domácí sítě aplikovat správnou cenovou dohodu pro hovory ukončené jeho účastníkovi v roamingu. Pro operátora navštívené sítě poskytuje jasnou identifikaci, že ukončovaný účastník je roamující, což spouští odpovídající účtování využití zdrojů a případné mezilehlé poplatky. Také podporuje pokročilé funkce hovorů, jako je zajištění, že hovor k roamujícímu účastníkovi nezpůsobí neúmyslně druhou, zbytečnou mezinárodní část kvůli neoptimálním rozhodnutím o směrování.

Z historické perspektivy, jak se roaming stal všudypřítomným, se ukázala potřeba úplné a symetrické sady signalizačních parametrů. VPLMNB doplnil obraz tím, že poskytl kontext navštívené sítě pro cíl hovoru, stejně jako to VPLMNA učinilo pro původ. To umožnilo plně automatizované, přesné a ověřitelné zpracování hovorů a finanční vypořádání pro oba konce mobilního hovoru, což bylo klíčové pro škálování mezinárodních mobilních služeb ziskově a spolehlivě.

## Klíčové vlastnosti

- Dynamická identifikace sítě pro volanou (B) stranu během roamingu
- Používá se v procedurách doručování a směrování mobilně ukončovaných hovorů
- Kritický pro přesné účtování ukončení a mezilehlá finanční vypořádání
- Umožňuje logiku služeb založených na poloze pro volanou stranu (např. podmíněné přesměrování)
- Přenášen v signalizaci mezi HLR, GMSC a VMSC
- Zajišťuje správné ukončení hovoru k obsluhující MSC v navštívené síti

## Související pojmy

- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [VPLMNA – Visited Public Land Mobile Network of the A subscriber](/mobilnisite/slovnik/vplmna/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain

---

📖 **Anglický originál a plná specifikace:** [VPLMNB na 3GPP Explorer](https://3gpp-explorer.com/glossary/vplmnb/)
