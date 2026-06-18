---
slug: "rand"
url: "/mobilnisite/slovnik/rand/"
type: "slovnik"
title: "RAND – RANDom number (authentication parameter)"
date: 2025-01-01
abbr: "RAND"
fullName: "RANDom number (authentication parameter)"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/rand/"
summary: "RAND je kritické náhodné číslo používané jako výzva v postupech 3GPP autentizace a dohody o klíčích (AKA). Generuje jej síť a zasílá se do uživatelského zařízení (UE) pro výpočet autentizačních odpově"
---

RAND je náhodné číslo generované sítí a používané jako výzva (challenge) v postupech 3GPP autentizace, které umožňuje uživatelskému zařízení (UE) vypočítat bezpečné odpovědi a odvodit reluční klíče.

## Popis

RAND (zkratka pro RANDom number – náhodné číslo) je základním 128bitovým parametrem v rámci bezpečnostní architektury 3GPP, konkrétně pro mechanismus Autentizace a dohody o klíčích ([AKA](/mobilnisite/slovnik/aka/)). Jedná se o kryptograficky silné náhodné nebo pseudonáhodné číslo generované autentizačním centrem sítě, které obvykle sídlí v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro LTE/5G nebo v Home Location Register/Authentication Centre ([HLR](/mobilnisite/slovnik/hlr/)/AuC) pro 2G/3G. Hlavní úlohou RANDu je sloužit jako náhodná výzva (challenge) v protokolu typu challenge-response. Během autentizačního postupu síť odešle RAND do uživatelského zařízení (UE) prostřednictvím obslužné sítě (např. [MME](/mobilnisite/slovnik/mme/), [SGSN](/mobilnisite/slovnik/sgsn/)).

Po přijetí předá UE RAND své aplikaci Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)). USIM, která sdílí dlouhodobý tajný klíč (K) s HSS/AuC, použije tento RAND spolu s klíčem K a dalšími parametry jako vstupy do sady kryptografických funkcí. Tyto funkce, standardizované v 3GPP (jako např. sada algoritmů MILENAGE), vytvoří dva klíčové výstupy: Podepsanou odpověď (Signed Response – [SRES](/mobilnisite/slovnik/sres/) pro 2G, [RES](/mobilnisite/slovnik/res/) pro 3G/4G/5G) a Šifrovací klíč (Cipher Key – CK) a Integritní klíč (Integrity Key – IK). UE odešle vypočítaný RES zpět do sítě. Síť, která vygenerovala stejný RAND a disponuje stejným tajným klíčem K, provede identický výpočet. Poté porovná RES přijatý od UE s RES, který vypočítala sama. Shoda prokazuje, že UE disponuje správným tajným klíčem, a je tedy autentická.

Kromě autentizace je RAND stejně zásadní i pro odvozování klíčů. Stejný výpočet, který vytváří RES, generuje i šifrovací klíč (CK) a integritní klíč (IK). Tyto klíče tvoří základ veškeré následné bezpečné komunikace mezi UE a sítí pro danou relaci. Používají se k odvození skutečných šifrovacích a integritních klíčů pro Přístupovou vrstvu (Access Stratum – AS) a Nepřístupovou vrstvu (Non-Access Stratum – NAS). Náhodnost a nepředvídatelnost RANDu je tudíž prvořadá. Slabý nebo předvídatelný RAND by mohl ohrozit celý autentizační proces, umožnit útoky opakováním (replay attacks) nebo usnadnit útočníkovi odhalení dlouhodobého tajného klíče. RAND zajišťuje, že každá instance autentizace je jedinečná, což poskytuje svěžest (freshness) a brání opětovnému použití dříve vyměněných autentizačních vektorů.

## K čemu slouží

RAND existuje za účelem poskytnutí robustní výzvy (challenge) v mechanismu autentizace typu challenge-response, který je klíčový pro zabezpečení celulárních sítí. Před standardizovanými autentizačními protokoly byly jednodušší systémy zranitelné vůči útokům opakováním (replay attacks), kdy útočník mohl zachytit a znovu odeslat platnou odpověď uživatele, aby získal přístup. Použití náhodné výzvy pro každý pokus o autentizaci tuto zranitelnost přířeč řeší. Tím, že je zajištěno, že výzva je pokaždé jiná, se dříve zaznamenaná odpověď pro útočníka stane nepoužitelnou.

Ve vývoji od GSM přes UMTS a dále se role RANDu rozšířila. V GSM byl RAND používán spolu s algoritmem COMP128 pro generování SRES a klíče Kc. Avšak autentizace GSM byla jednostranná (síť autentizuje UE) a měla kryptografické slabiny. Zavedení UMTS AKA počínaje Release 99 si RAND ponechalo, ale integrovalo jej do bezpečnějšího rámce vzájemné autentizace. RAND, kombinovaný s pořadovým číslem (SQN) pro zajištění svěžesti (freshness), se stal vstupem do silnějších algoritmů, které produkují oddělené klíče pro šifrování a integritu. Tím se vyřešila omezení slabší kryptografie GSM a absence ochrany integrity.

Motivace pro jeho vytvoření a pokračující používání spočívá v základní potřebě neopakující se, nepředvídatelné proměnné pro inicializaci kryptografických funkcí, které zabezpečují síť. Je to prvek, který zavádí entropii a variabilitu specifickou pro relaci do procesu generování klíčů. Bez nového RANDu pro každou autentizaci by mohly být odvozené reluční klíče předvídatelné, což by vedlo k fatálnímu selhání důvěrnosti a integrity uživatelských dat a signalizace. Jeho standardizace zajišťuje interoperabilitu mezi zařízeními od různých výrobců a sítěmi po celém světě.

## Klíčové vlastnosti

- 128bitové kryptograficky náhodné číslo používané jako síťová výzva (challenge)
- Primární vstup do autentizačních a klíčových generujících funkcí (např. MILENAGE)
- Zajišťuje svěžest (freshness) a brání útokům opakováním (replay attacks) v postupu AKA
- Generováno HSS/AuC a distribuováno do obslužné sítě v autentizačním vektoru
- Použito USIM pro výpočet autentizační odpovědi (RES) a relučních klíčů (CK, IK)
- Základní prvek pro zabezpečení přístupu k sítím 3G, 4G LTE a 5G

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [SQN – Sequence Number](/mobilnisite/slovnik/sqn/)
- [CKSN – Ciphering Key Sequence Number](/mobilnisite/slovnik/cksn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [RAND na 3GPP Explorer](https://3gpp-explorer.com/glossary/rand/)
