---
slug: "ocs"
url: "/mobilnisite/slovnik/ocs/"
type: "slovnik"
title: "OCS – Originating Call Screening"
date: 2026-01-01
abbr: "OCS"
fullName: "Originating Call Screening"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ocs/"
summary: "Doplňková služba v okruhově přepínaných (CS) sítích, která umožňuje účastníkovi omezit odchozí hovory na základě předdefinovaného seznamu. Umožňuje uživatelům nebo správcům blokovat hovory na konkrétn"
---

OCS je doplňková služba v okruhově přepínaných sítích, která umožňuje účastníkovi omezit odchozí hovory na základě předdefinovaného seznamu pro kontrolu a správu nákladů.

## Popis

Originating Call Screening (OCS, filtrování odchozích hovorů) je klasická doplňková služba v telekomunikacích standardizovaná organizací 3GPP pro okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) domény, včetně GSM a UMTS. Funguje jako síťový filtrační mechanismus aplikovaný na pokusy o hovor iniciované účastníkem. Když se uživatel pokusí uskutečnit hovor, je služební logika OCS vyvolána v domovském Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo ve navštíveném MSC. Služba porovná volané cílové číslo (kód základní služby a číslo volané strany) se screeningovým seznamem asociovaným s profilem účastníka. Tento seznam je uložen v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) účastníka a je stažen do obsluhujícího MSC/[VLR](/mobilnisite/slovnik/vlr/) během registrace nebo nastavování hovoru.

Logika filtrování je typicky založena na vzorcích nebo konkrétních číslech. Například seznam může obsahovat položky jako specifické kódy zemí (např. blokování všech mezinárodních hovorů), specifické směrová čísla nebo přesná telefonní čísla (např. blokování hovorů na konkrétní službu s prémiovou sazbou). Pokud dojde ke shodě mezi volaným číslem a zakázanou položkou v screeningovém seznamu, MSC přeruší proceduru nastavování hovoru. Uživatel je poté typicky upozorněn specifickou hláškou nebo tónem, že je hovor zakázán. Služba může být provozována s různou úrovní granularity, například filtrování všech hovorů, pouze pro určité přenosové služby (např. datové hovory) nebo pouze při roamingu.

Z architektonického hlediska OCS závisí na integraci mezi MSC, VLR a HLR. HLR uchovává profil služeb účastníka včetně OCS dat. Při zahájení hovoru MSC tato data načte z VLR (která je získala z HLR) a vykoná filtrační logiku. OCS je ukázkovým příkladem služby typu originating [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic) nebo nativní doplňkové služby založené na [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part). Jejím úkolem je poskytovat administrativní kontrolu, zabezpečení a omezení nákladů. Je široce používána v korporátním prostředí k zabránění neoprávněného využití, v předplacených systémech jako výchozí zákaz pro určité destinace a jednotlivými uživateli k zabránění náhodným hovorům na drahá čísla.

## K čemu slouží

OCS byla vyvinuta k řešení potřeby kontrolovaného a zabezpečeného využívání telefonie, zejména v kontextu mobilních sítí, kde mohou být poplatky za hovory významné. Před existencí takových síťových služeb bylo možné kontrolu odchozích hovorů zajistit pouze na straně terminálu (pokud vůbec) nebo prostřednictvím manuálního zásahu operátora, což nebylo škálovatelné. Primární problémy, které řeší, jsou správa nákladů, prevence podvodů a vynucování pravidel.

Pro firmy poskytující zaměstnancům mobilní telefony OCS zabraňuje zneužití blokováním hovorů na neautorizované nebo drahé destinace, jako jsou mezinárodní čísla nebo čísla s prémiovou sazbou. Pro síťové operátory je nástrojem pro řízení rizik u předplacených účastníků tím, že zakazuje destinace s vysokými náklady, které by mohly vést k nezaplaceným fakturám. Pro jednotlivé účastníky nabízí formu rodičovské kontroly nebo způsob, jak si sami nastavit výdajové limity. Její vznik byl motivován komerčními a provozními požadavky éry GSM, kde se doplňkové služby staly klíčovým diferenciátorem a zdrojem příjmů. OCS poskytla standardizovaný, na síti centrický způsob implementace těchto kontrol, což zajišťuje konzistentní chování napříč různými sítěmi i pro roamující účastníky.

## Klíčové vlastnosti

- Síťové filtrování pokusů o odchozí hovory.
- Používá účastníkovský screeningový seznam uložený v HLR.
- Podporuje filtrování na základě vzorců (např. kódy zemí, směrová čísla).
- Může být aktivována/deaktivována účastníkem nebo síťovým operátorem.
- Integruje se s CAMEL pro předplacené a inteligentní síťové služby.
- Poskytuje okamžité zakázání hovoru a upozornění uživatele při porušení pravidla.

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 28.849** (Rel-19) — CAPIF Phase2 Charging Study
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [OCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ocs/)
