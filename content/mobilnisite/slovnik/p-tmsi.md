---
slug: "p-tmsi"
url: "/mobilnisite/slovnik/p-tmsi/"
type: "slovnik"
title: "P-TMSI – Packet-Temporary Mobile Subscriber Identity"
date: 2025-01-01
abbr: "P-TMSI"
fullName: "Packet-Temporary Mobile Subscriber Identity"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/p-tmsi/"
summary: "Dočasná identita přidělená SGSN uživatelskému zařízení (UE) v paketově orientované doméně GPRS/UMTS. Chrání trvalý identifikátor IMSI uživatele před častým přenosem přes rozhraní, čímž zvyšuje bezpečn"
---

P-TMSI je dočasná identita přidělená SGSN uživatelskému zařízení (UE) v paketově orientované doméně GPRS/UMTS za účelem ochrany trvalého identifikátoru IMSI uživatele. Používá se pro signalizační procedury v jádru sítě.

## Popis

P-TMSI je klíčová identita v paketově orientovaném jádru sítě 2G [GPRS](/mobilnisite/slovnik/gprs/) a 3G UMTS. Jedná se o 32bitový dočasný identifikátor lokálně přidělený uzlem [SGSN](/mobilnisite/slovnik/sgsn/) uživatelskému zařízení (UE) po úspěšném připojení k paketově orientované doméně nebo při aktualizaci směrovací oblasti. Hlavním účelem P-TMSI je sloužit jako náhrada za trvalý identifikátor [IMSI](/mobilnisite/slovnik/imsi/) ve většině signalizačních zpráv mezi UE a sítí, čímž se minimalizuje vystavení citlivého IMSI. Struktura P-TMSI zahrnuje identitu SGSN, který jej přidělil (často prostřednictvím části [NRI](/mobilnisite/slovnik/nri/) – Network Resource Identifier), a lokální pořadové číslo. Když UE zahájí signalizační proceduru, například aktualizaci směrovací oblasti nebo služební požadavek, typicky k identifikaci vůči síti použije P-TMSI spolu s P-TMSI Signature (3bajtový autentizační token). Příjemní SGSN použije P-TMSI k vyhledání kontextu UE ve své databázi. Pokud kontext není nalezen (např. protože se UE přesunulo do oblasti nového SGSN), může síť zahájit proceduru žádosti o identitu pro získání IMSI uživatele. P-TMSI se periodicky nebo při specifických mobilních událostech znovu přiděluje za účelem zvýšení soukromí. Jeho platnost je omezena na směrovací oblast ([RA](/mobilnisite/slovnik/ra/)) a musí být aktualizováno, když se UE přesune do nové RA obsluhované jiným SGSN. P-TMSI úzce souvisí s procedurami připojení GPRS a aktualizací směrovací oblasti a je klíčovým parametrem při vytváření bezpečnostního kontextu mezi UE a SGSN.

## K čemu slouží

P-TMSI bylo zavedeno za účelem řešení kritických bezpečnostních a soukromých slabin spojených s přenosem trvalého [IMSI](/mobilnisite/slovnik/imsi/) přes rozhraní. Odesílání IMSI v čitelné formě (což bylo běžné v dřívějších systémech) by umožnilo odposlouchávajícím stranám sledovat polohu a identitu účastníka. P-TMSI poskytuje důvěrnost identity tím, že zajišťuje, aby se IMSI vysílalo jen velmi zřídka. Řeší problém sledovatelnosti účastníka a snižuje riziko útoků typu IMSI-catcher. Dále zlepšuje efektivitu signalizace; použití kratší, lokálně významné dočasné identity je efektivnější než přenos celého IMSI v každé zprávě. Jeho vznik byl motivován vývojem paketově orientovaného jádra pro [GPRS](/mobilnisite/slovnik/gprs/), které vyžadovalo vlastní identity pro správu mobility a relací oddělené od dočasné identity [TMSI](/mobilnisite/slovnik/tmsi/) v komutované doméně. P-TMSI spolu se svým podpisem také poskytuje mechanismus pro síť, aby mohla rychle ověřit nárok UE na identitu bez úplného ověřování při každé příležitosti, což urychluje mobilní procedury. Řešilo to omezení starších systémů, kterým chyběly robustní mechanismy dočasné identity pro datové služby.

## Klíčové vlastnosti

- 32bitová dočasná identita přidělená SGSN pro paketově orientovanou doménu.
- Nahrazuje IMSI ve většině signalizace přes rozhraní za účelem zvýšení soukromí a bezpečnosti účastníka.
- Používá se jako primární identifikátor UE v procedurách správy mobility GMM (např. Připojení a Aktualizace směrovací oblasti).
- Obvykle je doprovázena P-TMSI Signature pro ověření identity bez úplného ověřování.
- Má omezenou platnost, obvykle v oblasti řízené přidělujícím SGSN (Směrovací oblast).
- Je znovu přidělováno periodicky nebo při mobilitě mezi různými SGSN, aby se zabránilo dlouhodobému sledování.

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [P-TMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-tmsi/)
