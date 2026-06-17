---
slug: "cbc-mac"
url: "/mobilnisite/slovnik/cbc-mac/"
type: "slovnik"
title: "CBC-MAC – Cipher Block Chaining Message Authentication Code"
date: 2025-01-01
abbr: "CBC-MAC"
fullName: "Cipher Block Chaining Message Authentication Code"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cbc-mac/"
summary: "CBC-MAC je algoritmus kryptografického kódu pro ověření zprávy, který v systémech 3GPP poskytuje integritu dat a autentizaci. Funguje pomocí šifrování blokovou šifrou v režimu řetězení šifrových bloků"
---

CBC-MAC je kryptografický algoritmus v systémech 3GPP, který využívá šifrování blokovou šifrou v režimu řetězení šifrových bloků (CBC) k vytvoření autentizační značky pevné délky, čímž zajišťuje integritu dat a ověřuje autenticitu odesílatele.

## Popis

CBC-MAC je základní kryptografický primitiv používaný v bezpečnostních architekturách 3GPP k zajištění autentizace zpráv a ochrany integrity. Algoritmus funguje tak, že zpracovává otevřená data prostřednictvím blokové šifry v režimu řetězení šifrových bloků ([CBC](/mobilnisite/slovnik/cbc/)), kde je každý blok otevřeného textu před zašifrováním podroben operaci XOR s předchozím blokem šifrového textu. Konečný blok šifrového textu (nebo jeho část) slouží jako značka kódu pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)). Tato značka je připojena ke zprávě a příjemce ji ověří pomocí stejného tajného klíče a algoritmu.

Z architektonického hlediska je CBC-MAC implementován v bezpečnostních protokolech různých rozhraní a služeb 3GPP. Funguje jako klíčová součást mechanismů ochrany integrity jak v signalizaci řídicí roviny, tak v přenosu dat uživatelské roviny. Algoritmus vyžaduje symetrický tajný klíč sdílený mezi komunikujícími entitami, který je typicky stanoven prostřednictvím procedur autentizace a dohody o klíči. V systémech 3GPP se CBC-MAC často používá s konkrétními blokovými šiframi, jako je [AES](/mobilnisite/slovnik/aes/) (Advanced Encryption Standard) nebo Kasumi, v závislosti na generaci systému a bezpečnostních požadavcích.

Technické fungování začíná odsazením zprávy, aby byla zajištěna délka vstupu jako násobek velikosti bloku blokové šifry (typicky 128 bitů pro AES). Odsazená zpráva je rozdělena na bloky a proces CBC šifrování začíná inicializačním vektorem ([IV](/mobilnisite/slovnik/iv/)), který je v základním CBC-MAC často nastaven na nulu. Každý blok otevřeného textu je podroben operaci XOR s předchozím blokem šifrového textu (nebo s IV u prvního bloku) a poté je zašifrován pomocí blokové šifry a tajného klíče. Pouze konečný výstupní blok se stává hodnotou MAC, která představuje kryptografický kontrolní součet celé zprávy.

V sítích 3GPP hraje CBC-MAC klíčovou roli v mnoha bezpečnostních kontextech. Poskytuje ochranu integrity pro signalizační zprávy Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) mezi uživatelským zařízením a jádrem sítě, pro signalizaci Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) mezi UE a základnovou stanicí a pro data uživatelské roviny v určitých konfiguracích. Deterministická povaha algoritmu zajišťuje, že jakákoliv modifikace zprávy během přenosu povede při ověření k odlišné hodnotě MAC, což umožňuje detekci neoprávněných zásahů. Zatímco novější režimy autentizovaného šifrování, jako je AES-GCM, získaly na popularitě, CBC-MAC zůstává specifikován v normách 3GPP kvůli zpětné kompatibilitě a pro specifické případy použití, kde jsou jeho vlastnosti výhodné.

## K čemu slouží

CBC-MAC byl do systémů 3GPP zaveden k řešení základních bezpečnostních požadavků na autentizaci zpráv a integritu dat v telekomunikačních sítích. Před jeho přijetím měly rané mobilní systémy omezenou kryptografickou ochranu, což je činilo zranitelnými vůči padělání zpráv, opakovaným útokům a manipulaci s daty. Tato technologie řeší problém ověření, že přijaté zprávy pocházejí od legitimních zdrojů a nebyly během přenosu pozměněny, což je nezbytné pro integritu účtování, autorizaci služeb a bezpečnost sítě.

Vytvoření CBC-MAC v rámci 3GPP bylo motivováno potřebou standardizovaných, efektivních autentizačních mechanismů, které by mohly fungovat v rámci omezení mobilních zařízení a síťové infrastruktury. Na rozdíl od digitálních podpisů, které vyžadují asymetrickou kryptografii a infrastrukturu veřejných klíčů, CBC-MAC používá symetrickou kryptografii s nižší výpočetní náročností, což jej činí vhodným pro prostředí s omezenými zdroji. Jeho deterministický výstup a značka pevné délky umožňují její efektivní zařazení do hlaviček protokolů bez výrazného zvýšení režie.

Historický kontext ukazuje, že CBC-MAC řešil omezení dřívějších přístupů k autentizaci zpráv, které byly buď kryptograficky slabé, nebo příliš výpočetně náročné pro široké nasazení v mobilních sítích. Integrace algoritmu do norem 3GPP poskytla základ pro zabezpečenou komunikaci, která se vyvíjela přes několik generací při zachování zpětné kompatibility. Jeho pokračující specifikace napříč vydáními norem dokazuje jeho trvalou hodnotu jako stavebního kamene pro složitější bezpečnostní protokoly a jeho roli při zajišťování důvěryhodnosti buněčných komunikací.

## Klíčové vlastnosti

- Poskytuje autentizaci zpráv pomocí symetrické kryptografie
- Generuje autentizační značky pevné délky bez ohledu na délku zprávy
- Funguje v režimu řetězení šifrových bloků (CBC) pro kryptografické řetězení
- Podporuje ochranu integrity jak pro data řídicí, tak uživatelské roviny
- Lze implementovat s různými blokovými šiframi včetně AES a Kasumi
- Deterministický výstup umožňuje efektivní ověření na přijímací straně

## Související pojmy

- [AES – Advanced Encryption Standard](/mobilnisite/slovnik/aes/)

## Definující specifikace

- **TS 55.241** (Rel-19) — 3GPP Integrity Algorithm GIA4 Specification
- **TS 55.251** (Rel-19) — GEA5 and GIA5 Encryption Algorithm Specification

---

📖 **Anglický originál a plná specifikace:** [CBC-MAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbc-mac/)
