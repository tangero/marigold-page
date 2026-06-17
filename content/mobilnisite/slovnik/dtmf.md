---
slug: "dtmf"
url: "/mobilnisite/slovnik/dtmf/"
type: "slovnik"
title: "DTMF – Dual Tone Multiple Frequency"
date: 2026-01-01
abbr: "DTMF"
fullName: "Dual Tone Multiple Frequency"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dtmf/"
summary: "Signalizační metoda využívající páry audiofrekvencí k reprezentaci číslic a symbolů, umožňující řízení v pásmu (in-band) pro telefonní služby. Umožňuje uživatelům interakci s automatizovanými systémy,"
---

DTMF je signalizační metoda využívající páry audiofrekvencí k reprezentaci číslic a symbolů, umožňující řízení v pásmu (in-band) a interakci uživatele s automatizovanými systémy během hlasového hovoru.

## Popis

Dual Tone Multiple Frequency (DTMF) je signalizační systém v pásmu (in-band) pro telekomunikace, který využívá páry audiofrekvencí k zakódování číslic, písmen a symbolů. Každý klíč na telefonní klávesnici odpovídá jedinečné kombinaci dvou sinusových tónů – jedné z nízkofrekvenční skupiny (697 Hz, 770 Hz, 852 Hz, 941 Hz) a jedné z vysokofrekvenční skupiny (1209 Hz, 1336 Hz, 1477 Hz, 1633 Hz). Když uživatel stiskne klíč, tyto tóny jsou generovány současně a přenášeny přes hlasový kanál, což umožňuje přijímající straně dekódovat stisknutý klíč. DTMF je široce používán v telefonii pro interaktivní řízení, například při volání čísel, navigaci v automatizovaných menu a zadávání vstupu během hovorů.

V kontextu 3GPP sítí je DTMF signalizace integrována do různých specifikací základní síťové a servisní vrstvy, aby byla zajištěna interoperabilita přes okruhově a paketově orientované domény. Architektura zahrnuje generování DTMF tónů na uživatelském zařízení (UE) nebo síťových elementech, přenos přes hlasové nosiče a detekci aplikačními servery nebo síťovými uzly. Klíčové komponenty zahrnují DTMF generátor na UE, Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) pro zpracování tónů a aplikační server (např. pro systémy interaktivní hlasové odpovědi), který interpretuje tóny k vyvolání akcí. DTMF signály jsou přenášeny jako část hlasového proudu v okruhově orientovaných sítích nebo jako RTP payloady ve VoIP scénářích, s specifikacemi definujícími metody paketizace a transportu.

Technická operace začíná, když uživatel během hovoru stiskne klíč, což vyvolá generování odpovídajících DTMF tónů na UE. Tyto tóny jsou zakódovány do audio signálu a přeneseny přes zřízenou hlasovou cestu. V paketově orientovaných sítích jako IMS může být DTMF přenášeno pomocí RTP událostí (jak definuje RFC 4733) k zajištění spolehlivého doručení a k zabránění zkreslení z komprese kodeků. Přijímající entita, například [IVR](/mobilnisite/slovnik/ivr/) systém, využívá DTMF detektor k analýze audio proudu, identifikaci páru tónů a mapování na příkazy. Tento proces umožňuje funkce jako volání přípon, zadávání PINů nebo řízení služeb bez přerušení hovoru.

Role DTMF v 3GPP sítích přesahuje základní volání a podporuje pokročilé služby jako aktivace předávání hovoru, přístup k hlasové poště a řízení doplňkových služeb. Je specifikována přes více releasů k zachování zpětné kompatibility s legacy systémy při adaptaci na moderní IP architektury. Signalizace je klíčová pro interakci uživatele se síťovými službami, zajišťuje, že telefonní funkce jsou dostupné a funkční přes vyvíjající síťové technologie od 2G do 5G.

## K čemu slouží

DTMF byl vyvinut k nahrazení pulzního volání v telefonii, poskytuje rychlejší a spolehlivější metodu pro zasílání řídicích signálů během hovorů. Před DTMF používaly rotační volací zařízení pulzní signalizaci, která byla pomalá, náchylná na chyby a omezená pouze na volání čísel. DTMF zaváděl tónovou signalizaci, umožňující nejen rychlejší volání, ale také interaktivní možnosti, jako navigace v automatizovaných systémech a přístup ke rozšířeným službám. Tato inovace řešila potřebu efektivní signalizace v pásmu, která může koexistovat s hlasovým přenosem bez nutnosti separátních řídicích kanálů.

Historicky, DTMF se stal standardem s uvedením tónových telefonů v 60. letech a jeho adopce rostla s vzestupem automatizovaných telefonních služeb. Ve 3GPP standardech je DTMF zahrnuto od Release 2 k zajištění interoperability přes mobilní sítě, podporující jak okruhově orientované, tak následně paketově orientované hlasové služby. Řeší omezení předchozích signalizačních metod tím, že umožňuje detekci dvou tónů, která je robustní vůči šumu a kompatibilní s různými kodeky, což je klíčové pro systémy interaktivní hlasové odpovědi ([IVR](/mobilnisite/slovnik/ivr/)) a podporu legacy funkcí.

Motivace pro zahrnutí DTMF do 3GPP specifikací vychází z nutnosti zachovat bezproblémovou kontinuitu služeb při vývoji sítí od GSM k UMTS, LTE a 5G. Umožňuje kritické funkce jako bankovnictví přes telefon, řízení konferenčních hovorů a autentizaci služeb, které závisí na uživatelském vstupu během aktivních hovorů. Standardizací DTMF přes releasy 3GPP zajišťuje, že mobilní zařízení a síťové elementy mohou zpracovat tónovou signalizaci konzistentně, podporující tradiční telefonii i moderní VoIP aplikace, a tím spojuje legacy a služby další generace.

## Klíčové vlastnosti

- Signalizace v pásmu (in-band) využívající páry audiofrekvencí
- Kódování číslic (0-9), písmen (A-D) a symbolů (#, *)
- Podpora přenosu přes okruhově orientované i paketově orientované sítě
- Integrace se systémy interaktivní hlasové odpovědi (IVR)
- Spolehlivá detekce a interpretace síťovými aplikačními servery
- Zpětná kompatibilita s legacy telefonním zařízením

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 24.182** (Rel-19) — Customized Alerting Tones (CAT) Protocol
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.952** (Rel-19) — EVS Codec Selection, Verification & Characterization
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.976** (Rel-19) — AMR-WB Codec Characterization & Verification
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [DTMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtmf/)
