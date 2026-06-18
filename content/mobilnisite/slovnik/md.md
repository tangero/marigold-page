---
slug: "md"
url: "/mobilnisite/slovnik/md/"
type: "slovnik"
title: "MD – Message Digest"
date: 2025-01-01
abbr: "MD"
fullName: "Message Digest"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/md/"
summary: "V kontextu 3GPP se MD (Message Digest) typicky vztahuje k hodnotě hash SHA-1 používané pro ochranu integrity a autentizaci v různých bezpečnostních postupech. Jedná se o výstup kryptografické hashovac"
---

MD je hodnota hash SHA-1 používaná pro ochranu integrity a autentizaci v bezpečnostních postupech 3GPP, která zajišťuje, že data nebyla změněna.

## Popis

Ve specifikacích 3GPP znamená MD (Message Digest) nejčastěji implementovaný jako hodnota hash SHA-1 (Secure Hash Algorithm 1). Otisk zprávy (message digest) je pevně velká numerická reprezentace (hash) vstupní zprávy libovolné velikosti, generovaná kryptografickou hashovací funkcí. Jejím hlavním účelem je poskytnout ověření integrity dat; jakákoliv změna původní zprávy s extrémně vysokou pravděpodobností povede ke zcela odlišné hodnotě otisku. V systémech 3GPP jsou tyto otisky využívány v mnoha bezpečnostních mechanismech napříč různými síťovými rozhraními a protokoly.

Algoritmus SHA-1 zpracovává vstupní data v blocích, provádí řadu logických a aritmetických operací a vytváří 160bitový (20bytový) hash výstup, často reprezentovaný jako 40místný hexadecimální řetězec. V 3GPP je generování MD typicky specifikováno v rámci bezpečnostních postupů pro autentizaci a ochranu integrity. Může být například použito jako součást funkcí pro odvození klíčů, při výpočtu autentizačních vektorů (jako je [AUTN](/mobilnisite/slovnik/autn/) v autentizaci UMTS/LTE) nebo k ověření integrity signalizačních zpráv mezi síťovými prvky, jako jsou [MME](/mobilnisite/slovnik/mme/) a [HSS](/mobilnisite/slovnik/hss/).

Z architektonického hlediska není výpočet MD samostatnou síťovou funkcí, ale algoritmickou součástí integrovanou do různých bezpečnostních protokolů a síťových funkcí. Je využíván v postupech Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) definovaných v 3GPP TS 33.102 a souvisejících specifikacích. Home Subscriber Server (HSS) nebo Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) v 5G může použít tajný klíč (K) a další vstupy (jako [RAND](/mobilnisite/slovnik/rand/) a [SQN](/mobilnisite/slovnik/sqn/)) k výpočtu očekávaného otisku zprávy ([XMAC](/mobilnisite/slovnik/xmac/)), který je porovnán s otiskem (MAC) přijatým od uživatelského zařízení (UE), aby došlo k autentizaci UE a zajištění integrity zprávy.

Zatímco SHA-1 byl historickým standardem odkazovaným v mnoha vydáních 3GPP, jeho role je zásadní pro vytváření digitálních podpisů, hodnot pro kontrolu integrity a jako stavební blok pro složitější kryptografické operace. Použití MD zajišťuje, že kritická signalizace řídicí roviny a citlivá uživatelská data nemohou být během přenosu přes potenciálně nezabezpečená rádiová a jádrová síťová spojení pozměněna, čímž vytváří základ důvěry v mobilním ekosystému.

## K čemu slouží

Otisk zprávy (Message Digest, MD), konkrétně využívající SHA-1, byl začleněn do standardů 3GPP, aby poskytl standardizovanou, výpočetně efektivní metodu pro zajištění integrity dat a podporu autentizačních mechanismů. V raných vydáních 3GPP (3G/UMTS) existovala kritická potřeba zabezpečit novou paketovou doménu a ochránit signalizační zprávy před pozměněním a paděláním. Kryptografické hashovací funkce, jako je SHA-1, nabídly způsob, jak generovat kompaktní, jedinečný otisk zprávy, což příjemcům umožnilo ověřit, že data nebyla během přenosu změněna.

Hlavním problémem, který MD řeší, je poskytnutí prostředku pro kontrolu integrity v rámci bezpečnostních protokolů bez režie plného šifrování. Před rozšířením kanálů chráněných integritou mohly být signalizační zprávy zranitelné vůči útokům na modifikaci. Zahrnutím otisku zprávy vypočteného s tajným klíčem (což vede k Message Authentication Code neboli MAC) si síť a UE mohou vzájemně zajistit integritu kritických parametrů vyměňovaných během postupů, jako je připojení, aktualizace polohy a předání. Tím se zabrání tomu, aby útočníci mohli měnit zprávy například za účelem přesměrování provozu nebo snížení úrovně zabezpečení.

Motivace pro použití SHA-1 pramenila z jeho statusu standardizovaného NIST, široce prověřeného a v době standardizace 3G relativně rychlého algoritmu. Řešil omezení dřívějších slabších metod kontrolních součtů, které neposkytovaly žádnou kryptografickou bezpečnost. S rozvojem kryptografického výzkumu však byly u SHA-1 objeveny zranitelnosti, což vedlo k jeho zavržení pro určité použití. Pozdější vydání 3GPP se vyvinula tak, aby podporovala silnější hashovací algoritmy (jako SHA-256) pro nové funkce, ale pojem "MD" a jeho základní koncept zůstávají nedílnou součástí bezpečnostní architektury. Jeho zavedení bylo motivováno potřebou robustního, standardizovaného kryptografického primitiva, které by mohlo být spolehlivě implementováno ve všech síťových prvcích a uživatelských zařízeních po celém světě.

## Klíčové vlastnosti

- Kryptografický hash výstup (typicky 160bitový pro SHA-1) používaný jako hodnota pro kontrolu integrity
- Nedílná součást postupů Authentication and Key Agreement (AKA) v 3GPP
- Používán k generování Message Authentication Codes (MAC) pro integritu signalizace
- Vstup pro funkce odvození klíčů při generování šifrovacích a integritních klíčů
- Standardizovaný algoritmus (SHA-1) zajišťující interoperabilitu mezi dodavateli
- Poskytuje ověření integrity dat, což zajišťuje, že zprávy nejsou během přenosu změněny

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TR 35.937** (Rel-19) — MILENAGE-256 Algorithm Set Specification

---

📖 **Anglický originál a plná specifikace:** [MD na 3GPP Explorer](https://3gpp-explorer.com/glossary/md/)
