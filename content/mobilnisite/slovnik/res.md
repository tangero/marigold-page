---
slug: "res"
url: "/mobilnisite/slovnik/res/"
type: "slovnik"
title: "RES – Authentication Response"
date: 2025-01-01
abbr: "RES"
fullName: "Authentication Response"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/res/"
summary: "RES je klíčový autentizační parametr v systémech 3GPP. V 3G Authentication and Key Agreement (AKA) je to odpověď generovaná USIM a ověřovaná sítí pro autentizaci uživatele. V 2G je to autentizační hod"
---

RES je autentizační odpověď generovaná USIM v 3G nebo poskytnutá HLR/AuC v 2G, kterou síť ověřuje, aby prokázala identitu účastníka pro zabezpečený přístup.

## Popis

Authentication Response (RES) je klíčový prvek v bezpečnostní architektuře 3GPP, konkrétně v rámci procedur autentizace a dohody o klíčích. Jedná se o kryptograficky generovanou hodnotu, která slouží jako důkaz identity z uživatelské strany. V proceduře 3G [AKA](/mobilnisite/slovnik/aka/) je RES vytvořen kartou Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) uvnitř User Equipment (UE). Síťová strana, konkrétně Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) obsluhující sítě nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))/Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) v pozdějších generacích, uchovává očekávanou autentizační odpověď ([XRES](/mobilnisite/slovnik/xres/)), kterou obdržela od Authentication Centre (AuC) domovské sítě.

Proces začíná, když síť odešle autentizační výzvu (challenge) k UE, která zahrnuje náhodné číslo ([RAND](/mobilnisite/slovnik/rand/)) a autentizační token ([AUTN](/mobilnisite/slovnik/autn/)). USIM použije svůj sdílený tajný klíč (K), bezpečně uložený na SIM/USIM, spolu s přijatým RAND a procesem ověření pořadového čísla, aby vypočítal dvě hodnoty: šifrovací klíč (CK) a integritní klíč (IK) pro zabezpečení následné komunikace, a RES. USIM odešle vypočítaný RES zpět do sítě. Síťová entita porovná přijatý RES s XRES, který si předem vypočítala nebo obdržela od AuC. Pokud se RES shoduje s XRES, je autentizace úspěšná, což dokazuje, že UE disponuje správným tajným klíčem, a je tedy legitimním účastníkem. Síť následně přistoupí k použití odvozených CK a IK pro šifrování a integritní ochranu rádiového spojení.

V kontextu 2G (GSM) autentizace je termín RES také používán, ale architektura se liší. Home Location Register (HLR) a jeho přidružené AuC vygenerují tripletu skládající se z RAND, Signed Response (SRES – ekvivalent XRES) a šifrovacího klíče Kc. Tato tripleta je odeslána obsluhujícímu MSC/VLR. VLR odešle RAND k Mobile Station (MS). SIM karta v MS vypočte vlastní SRES (odpověď) pomocí svého tajného klíče Ki a odešle jej zpět. VLR porovná SRES od MS s SRES z triolety pro autentizaci. Ať už tedy v 2G nebo 3G AKA, RES/SRES je kryptografická odpověď účastníka na síťovou výzvu a tvoří základ vzájemné autentizace (v 3G) nebo autentizace uživatele sítí (v 2G).

## K čemu slouží

RES existuje, aby poskytl síti bezpečnou metodu pro ověření identity účastníka, který se pokouší přistoupit k jejím službám. Před standardy mobilní autentizace mohly podvodná zařízení snadno vydávat za legitimní uživatele, což vedlo k podvodům (klonování) a krádežím služeb. RES jako součást protokolu typu challenge-response tento problém řeší tím, že vyžaduje, aby UE prokázalo znalost tajného klíče (K nebo Ki), aniž by tento klíč sám o sobě byl kdy přenášen vzduchem.

Vytvoření mechanismu RES v GSM (jako SRES) řešilo zranitelnost jednoduchého přenosu hesla. Procedura 3G AKA toto vylepšila zavedením vzájemné autentizace a silnějších kryptografických algoritmů. RES v 3G AKA je součástí robustnějšího rámce, který také poskytuje separaci klíčů a odvozování nových klíčů pro každou relaci, čímž řeší omezení 2G, jako je absence autentizace sítě vůči uživateli a slabší šifrování. RES je tedy klíčový pro prevenci neoprávněného přístupu, ochranu soukromí uživatele a vytvoření základu pro odvození relaních klíčů, které zabezpečují hlasovou a datovou komunikaci.

## Klíčové vlastnosti

- Kryptografický výstup generovaný USIM (3G) nebo SIM (2G)
- Prokazuje identitu účastníka prostřednictvím mechanismu challenge-response
- Porovnává se s očekávanou hodnotou sítě (XRES/SRES) pro autentizaci
- Odvozen pomocí sdíleného tajného klíče (K/Ki) a náhodné výzvy (RAND)
- Základní pro proceduru 3G Authentication and Key Agreement (AKA)
- Používá se také v 2G GSM autentizaci (jako SRES, součást autentizační triolety)

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [RAND – RANDom number (authentication parameter)](/mobilnisite/slovnik/rand/)
- [CKSN – Ciphering Key Sequence Number](/mobilnisite/slovnik/cksn/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [RES na 3GPP Explorer](https://3gpp-explorer.com/glossary/res/)
