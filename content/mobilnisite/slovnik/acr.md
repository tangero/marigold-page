---
slug: "acr"
url: "/mobilnisite/slovnik/acr/"
type: "slovnik"
title: "ACR – Anonymous Communications Rejection"
date: 2026-01-01
abbr: "ACR"
fullName: "Anonymous Communications Rejection"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acr/"
summary: "ACR je doplňková služba v sítích 3GPP, která umožňuje uživateli automaticky odmítat příchozí hovory nebo relace od účastníků, kteří skryli identitu volající linky (CLI). Chrání soukromí uživatele tím,"
---

ACR je doplňková služba, která automaticky odmítá příchozí hovory nebo relace od účastníků, kteří skryli identitu volající linky, aby chránila soukromí uživatele a zabránila nežádoucímu kontaktu.

## Popis

Anonymous Communications Rejection (ACR, odmítnutí anonymní komunikace) je standardizovaná doplňková služba definovaná v rámci specifikací 3GPP, primárně pro sítě založené na přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) a na IP Multimedia Subsystem (IMS). Funguje jako síťová funkce, kterou typicky poskytuje a spravuje operátor jménem účastníka. Hlavní funkcí ACR je zachytit příchozí pokusy o komunikaci – jako jsou hlasové hovory nebo v IMS potenciálně i jiné typy relací – a analyzovat identifikační informace volající strany. Klíčovým parametrem je stav prezentace identity volající linky ([CLI](/mobilnisite/slovnik/cli/)), známé také jako číslo volající strany. Pokud je příchozí požadavek označen indikátorem prezentace znamenajícím 'anonymní', 'zatajené' nebo 'omezené', je aktivována servisní logika ACR. Síť poté zabrání dokončení hovoru na terminál volaného uživatele a typicky vrátí volajícímu specifický tón, hlášení nebo kód [SIP](/mobilnisite/slovnik/sip/) odpovědi (např. 403 Forbidden), což signalizuje, že hovor byl odmítnut z důvodu anonymity.

Z architektonického hlediska pro CS sítě sídlí servisní logika ACR v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo v Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) obsluhujícím účastníka. MSC/VLR kontroluje profil služeb účastníka, který zahrnuje stav předplatného ACR, proti indikátoru prezentace v příchozí zprávě pro sestavení hovoru (např. [ISUP](/mobilnisite/slovnik/isup/) Initial Address Message). Pro IMS sítě je servisní logika implementována v rámci Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) aplikací počátečních filtračních kritérií (iFC), která směrují příchozí požadavek SIP INVITE na aplikační server ([AS](/mobilnisite/slovnik/as/)) hostující službu ACR. AS vyhodnocuje hlavičku SIP P-Asserted-Identity nebo hlavičku 'From' s nastavením ochrany soukromí, aby určil, zda je identita prezentována. Rozhodnutí služby (povolit nebo odmítnout) je poté vynuceno S-CSCF.

Služba je vysoce konfigurovatelná. Účastníci mohou ACR typicky aktivovat nebo deaktivovat prostřednictvím síťového managementu, jako jsou kódy Unstructured Supplementary Service Data (USSD) nebo přes zákaznický portál. Některé implementace mohou umožňovat podrobnější kontrolu, například vytvoření výjimečného seznamu ('white list') konkrétních anonymních čísel, kterým je povoleno spojení. Služba úzce spolupracuje s dalšími doplňkovými službami, jako je Calling Line Identification Presentation (CLIP) a Calling Line Identification Restriction (CLIR). ACR v podstatě poskytuje inverzní logiku k CLIP; zatímco CLIP umožňuje volané straně vidět číslo, ACR jí umožňuje blokovat hovory, když toto číslo není prezentováno. Její role je zásadní pro uživatelsky orientované soukromí a kontrolu v telekomunikacích, funguje jako vrátný, který vynucuje preferenci volané strany komunikovat pouze s identifikovatelnými volajícími.

## K čemu slouží

Hlavním účelem ACR je poskytnout účastníkům sítě kontrolu nad jejich komunikací a zvýšit jejich soukromí. Před standardizací takových služeb neměli uživatelé přijímající hovory od anonymních stran žádný síťově asistovaný prostředek k jejich odfiltrování; museli hovor přijmout nebo jej nechat přejít do hlasové schránky, aby zjistili volajícího, což mohlo vést k obtěžování, spamu nebo nežádoucí telemarketingu. ACR tento problém řeší poskytnutím automatizované bariéry vynucené sítí. Řeší společenské a soukromí týkající se obav plynoucích ze samotné schopnosti omezení prezentace identity volající linky (CLIR), která volajícím umožňuje zatajit své číslo. Zatímco CLIR je legitimním nástrojem ochrany soukromí pro volající, ACR vyvažuje ekosystém tím, že dává volané straně rovnocenné právo takové anonymní interakce odmítnout.

Historicky byl vývoj ACR v 3GPP Release 7 součástí širšího zrání doplňkových služeb pro GSM a UMTS a jejich rozšíření do vznikající architektury IMS. Formalizoval službu, která existovala v různých proprietárních formách ve fixních sítích a raných mobilních sítích. Standardizace zajistila interoperabilitu mezi různými síťovými operátory a dodavateli zařízení, což umožnilo účastníkům spolehlivě používat službu i při roamingu. Řešila omezení čistě terminálových řešení (jako jsou blokovací seznamy na telefonu), která mohla být obejita nebo nebyla všeobecně dostupná. Jako síťově centrická služba poskytuje ACR konzistentní chování bez ohledu na typ nebo schopnosti uživatelského telefonu a k odmítnutí dochází před tím, než hovor zazvoní na terminálu, čímž šetří baterii a zabraňuje vyrušování.

## Klíčové vlastnosti

- Automaticky odmítá hovory/relace se zatajenou nebo omezenou identitou volající linky (CLI)
- Síťová servisní logika umístěná v MSC/VLR pro CS a v S-CSCF/AS pro IMS
- Konfigurovatelná aktivace/deaktivace prostřednictvím USSD nebo rozhraní pro správu služeb
- Spolupracuje se službami Calling Line Identification Presentation (CLIP) a Restriction (CLIR)
- Poskytuje specifické tóny nebo SIP odpovědi (např. 403) odmítnutým anonymním volajícím
- Podporuje potenciální seznamy výjimek ('white list') pro povolená anonymní čísla

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [CLIR – Calling Line Identification Restriction](/mobilnisite/slovnik/clir/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- … a dalších 41 specifikací

---

📖 **Anglický originál a plná specifikace:** [ACR na 3GPP Explorer](https://3gpp-explorer.com/glossary/acr/)
