---
slug: "usf"
url: "/mobilnisite/slovnik/usf/"
type: "slovnik"
title: "USF – Uplink State Flag"
date: 2025-01-01
abbr: "USF"
fullName: "Uplink State Flag"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/usf/"
summary: "Řídicí pole používané v GSM/EDGE a GPRS při přidělování rádiových zdrojů k dynamickému udělení práv pro přenos v uplinku konkrétní mobilní stanici na sdíleném kanálu pro paketová data. Umožňuje efekti"
---

USF je řídicí pole používané v GSM/EDGE a GPRS k dynamickému udělení práva konkrétní mobilní stanici vysílat na sdíleném kanálu pro paketová data v uplinku, což umožňuje efektivní multiplexování.

## Popis

Uplink State Flag (USF, příznak stavu uplinku) je základní mechanismus plánování v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)) pro paketově orientované služby jako [GPRS](/mobilnisite/slovnik/gprs/) a EDGE. Jedná se o malý identifikátor (typicky 3 bity) vysílaný na downlinku systémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) k řízení toho, které mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) je povoleno vysílat v uplinku v následujících rádiových blocích na sdíleném kanálu pro paketová data ([PDCH](/mobilnisite/slovnik/pdch/)). Každý časový slot PDCH může být v uplinku sdílen více MS a USF poskytuje nezbytnou arbitráž k zabránění kolizím, fungující na principu "dotazování" nebo "udělování" práva.

USF pracuje v kontinuálním cyklu na bázi jednotlivých časových slotů. Na downlinku každý rádiový blok (skupina čtyř normálních burstů) vysílaný na PDCH nese v hlavičce hodnotu USF. Tato hodnota USF odpovídá konkrétnímu dočasnému toku bloků ([TBF](/mobilnisite/slovnik/tbf/)) – dočasnému logickému spojení pro přenos dat v uplinku jedné MS. Když je MS přiřazen uplinkový TBF, je jí zároveň přidělena hodnota USF. MS musí nepřetržitě monitorovat downlinkové bloky na svém přiděleném PDCH. Když detekuje downlinkový blok obsahující jí přidělenou hodnotu USF, interpretuje to jako povolení k vyslání vlastního rádiového bloku v uplinku v následujícím odpovídajícím rádiovém bloku na stejném časovém slotu. Tím vzniká těsný, předvídatelný plán: povolení v downlinkovém bloku N umožňuje přenos v uplinkovém bloku N+1.

Z architektonického hlediska USF spravuje jednotka řízení paketů ([PCU](/mobilnisite/slovnik/pcu/)) v rámci BSS, která funguje jako plánovač. PCU přiřazuje hodnoty USF při zakládání uplinkových TBF a je zodpovědná za dynamické přidělování uplinkových zdrojů na základě stavu vyrovnávací paměti MS, požadavků na QoS a algoritmů spravedlivosti. Mechanismus USF je klíčový pro fungování kanálu pro paketová data v uplinku (PDTCH), což je fyzický kanál přenášející uživatelská data. Použitím USF dosahuje GERAN statistického multiplexování pro paketová data v uplinku, což síti umožňuje obsloužit mnohem více současných datových uživatelů, než je fyzických časových slotů, což výrazně zlepšuje spektrální účinnost pro přerušovaný datový provoz ve srovnání s přepojováním okruhů.

## K čemu slouží

USF byl zaveden ve specifikacích GSM Phase 2+ s plnou standardizací pro GPRS ve 3GPP Release 5 (ačkoli komerčně byl nasazen dříve). Byl vytvořen k vyřešení základního problému sdíleného přístupu k médiu v uplinku pro buněčná paketová data. Před GPRS bylo GSM čistě okruhově orientované a vyčleňovalo celý časový slot pro jeden hovor po celou jeho dobu – což byl pro přerušované datové přenosy neefektivní model.

USF umožnil centralizovaný, plánovaný přístup k uplinku, což bylo pro buněčné prostředí zásadní. Alternativní metody jako náhodný přístup (používaný pro úvodní signalizaci) nebo protokoly s kolizemi (jako CSMA v Ethernetu) byly nevhodné kvůli problému skryté stanice, vysoké pravděpodobnosti kolizí a neschopnosti garantovat QoS. USF poskytl deterministickou metodu bez kolizí, která síti umožnila řídit a arbitrovat uplinkové přenosy od více mobilních stanic na stejném fyzickém zdroji. To umožnilo operátorům GSM zavést efektivní služby paketových dat bez nutnosti hardwarových změn rádiového rozhraní, s využitím stávající struktury časových slotů. Byla to klíčová inovace, která učinila GPRS a později EDGE životaschopnými a přeměnila GSM ze sítě pouze pro hlas na platformu pro mobilní data.

## Klíčové vlastnosti

- 3bitový identifikátor vysílaný v downlinkových rádiových blocích k udělení práv pro přenos v uplinku
- Umožňuje dynamické plánování více mobilních stanic na sdíleném kanálu pro paketová data v uplinku (PDCH) na úrovni jednotlivých bloků
- Poskytuje přístup k uplinku bez kolizí prostřednictvím centralizované síťové kontroly
- Funguje v součinnosti s dočasnými toky bloků (TBF) pro paketové datové relace
- Základní prvek mechanismů přidělování zdrojů v uplinku pro GPRS a EDGE
- Umožňuje efektivní statistické multiplexování přerušovaného datového provozu na časových slotech GSM

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PDTCH – Packet Data Traffic Channel](/mobilnisite/slovnik/pdtch/)
- [PCU – Packet Control Unit](/mobilnisite/slovnik/pcu/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study
- **TS 45.871** (Rel-14) — MIMO for GSM/EDGE Downlink Study

---

📖 **Anglický originál a plná specifikace:** [USF na 3GPP Explorer](https://3gpp-explorer.com/glossary/usf/)
