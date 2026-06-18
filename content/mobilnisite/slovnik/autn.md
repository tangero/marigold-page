---
slug: "autn"
url: "/mobilnisite/slovnik/autn/"
type: "slovnik"
title: "AUTN – Authentication Token"
date: 2026-01-01
abbr: "AUTN"
fullName: "Authentication Token"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/autn/"
summary: "AUTN je token generovaný sítí používaný v protokolech 3GPP pro autentizaci a dohodu klíčů (AKA). Autentizuje síť vůči uživatelskému zařízení (UE), čímž prokazuje legitimitu a brání útokům, jako je man"
---

AUTN je token generovaný sítí používaný v protokolech 3GPP AKA k autentizaci sítě vůči uživatelskému zařízení, čímž prokazuje její legitimitu a umožňuje vzájemnou autentizaci.

## Popis

Autentizační token (AUTN) je klíčová součást rámce 3GPP pro autentizaci a dohodu klíčů ([AKA](/mobilnisite/slovnik/aka/)), používaného v systémech UMTS, LTE a 5G. Je generován Autentizačním centrem (AuC) sítě a odeslán uživatelskému zařízení (UE) jako součást autentizačního vektoru během hlavního autentizačního postupu. AUTN má jediný, zásadní účel: autentizovat obsluhující síť vůči UE. Tím je zajištěna vzájemná autentizace, neboť se i UE autentizuje vůči síti pomocí samostatného parametru odpovědi ([RES](/mobilnisite/slovnik/res/)).

Technicky je AUTN zřetězený bitový řetězec složený z několika dílčích komponent. Hlavními prvky jsou kód pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)) a pořadové číslo ([SQN](/mobilnisite/slovnik/sqn/)). MAC je vypočítán AuC pomocí tajného klíče účastníka (K) a sady vstupních parametrů včetně SQN, náhodné výzvy ([RAND](/mobilnisite/slovnik/rand/)) a identifikátoru obsluhující sítě. Tento MAC dokazuje, že token pochází od legitimní entity disponující správným klíčem. SQN je parametr čerstvosti, který zajišťuje, že autentizační požadavek je nový, a chrání před útoky opakováním. UE, které také disponuje tajným klíčem K, nezávisle vypočítá očekávaný MAC ([XMAC](/mobilnisite/slovnik/xmac/)) z přijatých hodnot RAND a SQN. Pokud se vypočtený XMAC shoduje s MAC uvnitř AUTN, je síť ověřena jako autentická.

Po přijetí AUTN provede UE několik kontrol. Nejprve ověří MAC, aby potvrdilo autenticitu sítě. Za druhé zkontroluje SQN, aby zajistilo, že je v přijatelném rozsahu, čímž potvrdí čerstvost požadavku a zabrání síti znovu použít staré autentizační vektory. Pokud tyto kontroly projdou, UE považuje síť za legitimní a pokračuje v generování své autentizační odpovědi. Úspěšné ověření AUTN spustí odvození šifrovacího klíče ([CK](/mobilnisite/slovnik/ck/)) a klíče integrity ([IK](/mobilnisite/slovnik/ik/)) ze stejného tajného klíče K a hodnoty RAND, čímž se stanoví bezpečné klíče pro následnou šifrovanou a integritně chráněnou komunikaci.

V celkové síťové architektuře je AUTN součástí autentizačního vektoru (AV), typicky kvintetu (pro 3G/4G) nebo vektoru (pro 5G), který zahrnuje RAND, AUTN, XRES (Očekávaná odpověď), CK a IK. Tento vektor je generován AuC/ARPF (Autentizační úložiště a zpracovatelská funkce) a doručen uzlu obsluhující sítě (např. VLR/SGSN/MME/AMF). Obsluhující uzel poté přepošle RAND a AUTN k UE, aby zahájil výzvu. Role AUTN je tedy klíčová v počátečním handshake, který naváže důvěryhodný vztah před výměnou jakýchkoli uživatelských dat.

## K čemu slouží

AUTN byl vytvořen, aby vyřešil kritickou bezpečnostní slabinu předchozích generací mobilních sítí (např. GSM), které poskytovaly pouze jednosměrnou autentizaci (síť autentizuje uživatele). Tato asymetrie činila systémy zranitelnými vůči útokům falešnou základnovou stanicí, kdy by škodlivý síťový prvek mohl vydávat za legitimního operátora, aby zachytil komunikaci nebo sledoval uživatele. Primárním účelem AUTN je umožnit vzájemnou autentizaci, aby si UE mohlo ověřit, že se připojuje ke skutečné, autorizované 3GPP síti.

Historicky byla bezpečnost GSM založena na sdíleném tajemství (Ki) a mechanismu výzva-odpověď, ale legitimita sítě nebyla mobilnímu zařízení nikdy kryptograficky prokázána. Zavedení AUTN v 3G UMTS (Release 99) jako součásti protokolu UMTS AKA tento paradigma zásadně změnilo. Vyřešilo problém autentizace sítě poskytnutím ověřitelného tokenu, čímž zmírnilo útoky man-in-the-middle a vydávání se za někoho jiného. Tato evoluce byla nezbytná pro podporu nových služeb, rostoucích obav o ochranu dat a zvyšující se hodnoty mobilních transakcí.

Dále AUTN prostřednictvím SQN zahrnuje čerstvost, která řeší útoky opakováním, kdy by útočník mohl zachytit a znovu použít staré autentizační zprávy. Tím, že nutí síť prokázat, že používá novou, sekvenčně vhodnou výzvu, zajišťuje AUTN, že celá autentizační výměna je aktuální a bezpečná. Tato kombinace kontrol autenticity a čerstvosti tvoří základ důvěry pro veškerou následnou zabezpečenou komunikaci v 3GPP sítích, od hlasových hovorů v 3G po vysokorychlostní data a služby IoT v 4G a 5G.

## Klíčové vlastnosti

- Poskytuje autentizaci sítě vůči UE, čímž umožňuje vzájemnou autentizaci
- Obsahuje kód pro ověření zprávy (MAC) pro kryptografický důkaz původu
- Zahrnuje pořadové číslo (SQN) pro zajištění čerstvosti a prevenci útoků opakováním
- Po úspěšném ověření spouští odvození šifrovacího klíče a klíče integrity (CK/IK)
- Základní komponenta autentizačních vektorů v postupech AKA pro UMTS, LTE a 5G
- Generován Autentizačním centrem (AuC)/ARPF pomocí tajného klíče účastníka (K)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps

---

📖 **Anglický originál a plná specifikace:** [AUTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/autn/)
