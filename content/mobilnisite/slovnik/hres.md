---
slug: "hres"
url: "/mobilnisite/slovnik/hres/"
type: "slovnik"
title: "HRES – Hash RESponse"
date: 2026-01-01
abbr: "HRES"
fullName: "Hash RESponse"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hres/"
summary: "Kryptografická hodnota generovaná modulem univerzální identity účastníka (USIM) během procesu 5G Authentication and Key Agreement (AKA). HRES je odpověď USIM na výzvu sítě, odvozená z tajného klíče a"
---

HRES je kryptografická odpověď generovaná USIM během 5G AKA, odvozená z tajného klíče a náhodné výzvy sítě za účelem ověření autenticity účastníka.

## Popis

HRES (Hash RESponse) je klíčový výstup kryptografických funkcí prováděných modulem univerzální identity účastníka ([USIM](/mobilnisite/slovnik/usim/)) během procedur 5G Authentication and Key Agreement (5G [AKA](/mobilnisite/slovnik/aka/)) a EPS AKA. Jedná se o 128bitovou hodnotu, která slouží jako důkaz účastníkova držení sdíleného tajného klíče (K). Generování HRES je kritickým krokem v oboustranné autentizaci mezi uživatelským zařízením (UE) a sítí. Proces začíná, když síťová funkce Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) prostřednictvím obsluhující sítě (např. [AMF](/mobilnisite/slovnik/amf/)/[SEAF](/mobilnisite/slovnik/seaf/)) odešle do UE autentizační vektor. Tento vektor obsahuje náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)) a autentizační token ([AUTN](/mobilnisite/slovnik/autn/)).

UE předá RAND a AUTN aplikaci USIM. USIM nejprve ověří AUTN, aby autentizovala síť a zajistila, že komunikuje s legitimní sítí, která také disponuje správným tajným klíčem (K). Pokud autentizace sítě uspěje, USIM přistoupí k výpočtu odpovědi. Pomocí sdíleného tajného klíče (K) bezpečně uloženého v USIM a přijatého RAND provede USIM sadu algoritmů Milenage nebo TUAK. Tento algoritmus generuje několik výstupů, včetně šifrovacího klíče ([CK](/mobilnisite/slovnik/ck/)), integritního klíče (IK) a odpovědi (RES). V 5G, pro zvýšení ochrany soukromí, není RES přenášen přes rozhraní v otevřené podobě. Místo toho UE (konkrétně ME - Mobile Equipment) spočítá hash hodnoty RES a vytvoří HRES. Použitá hashovací funkce je definována v 3GPP TS 33.501, typicky se jedná o hash s klíčem nebo kryptografický hash jako SHA-256, v závislosti na kontextu.

HRES je následně přenesen UE do obsluhující sítě (např. do SEAF v AMF). Strana sítě, která původně vygenerovala autentizační vektor v domovské síti (HN), má uloženou očekávanou odpověď (XRES). HN také spočítá hash hodnoty XRES, nazývaný HXRES. Obsluhující síť přijme HRES od UE a porovná jej s HXRES přijatým od HN. Pokud se HRES rovná HXRES, dokazuje to, že USIM vygeneroval správný RES, což následně dokazuje, že disponuje platným tajným klíčem K. Tím je dokončena autentizace účastníka. Odvození HRES z RES je v 5G opatřením pro ochranu soukromí, neboť zabraňuje odposlouchávající straně získat otevřený RES, který by mohl být použit ke sledování účastníka napříč různými obsluhujícími sítěmi.

HRES tedy funguje jako autentizační přihlašovací údaj chránící soukromí. Jeho správnost je základem pro to, aby síť mohla pokračovat v odvozování klíčů a navázala bezpečné šifrovací a integritní klíče (K_AMF, K_SEAF), které zabezpečí veškerou následující signalizaci NAS a RRC i uživatelská data. Celý proces zajišťuje, že pouze UE s platným USIM a tajným klíčem může přistupovat k síti, a zároveň chrání dlouhodobou identitu účastníka před vystavením na rádiovém rozhraní.

## K čemu slouží

HRES existuje jako základní součást bezpečnostního rámce 3GPP pro provádění autentizace účastníka a zároveň řeší konkrétní bezpečnostní hrozby a hrozby pro soukromí. Jeho primárním účelem je umožnit obsluhující síti ověřit, že UE disponuje správným sdíleným tajným klíčem (K), aniž by tento klíč sama znala, v souladu s principem autentizace a dohody o klíči (AKA). Řešeným problémem je prokázání identity účastníka kryptograficky bezpečným způsobem, který je odolný vůči opakovaným útokům a odposlechu.

Vývoj od RES k HRES v 5G byl motivován obavami o soukromí identifikovanými v předchozích generacích (4G/LTE). V LTE AKA byl otevřený RES odesílán z UE do sítě. Ačkoli je RES sám o sobě dočasnou hodnotou, jeho přenos v otevřené podobě přes rádiové rozhraní mohl být potenciálně využit pasivním pozorovatelem k otiskování a sledování účastníka při jeho pohybu mezi různými obsluhujícími sítěmi nebo dokonce buňkami. 5G zavedlo silnější důraz na ochranu soukromí identity účastníka. Hashováním RES za účelem vytvoření HRES je hodnota přenášená vzduchem kryptograficky transformována. To činí výpočetně neproveditelným, aby odposlouchávající strana mohla spojit hodnoty HRES z různých autentizačních relací zpět ke stejnému účastníkovi nebo k otevřenému RES, čímž se zmírňují útoky sledování.

HRES navíc usnadňuje oddělení odpovědností za autentizaci mezi domovskou sítí (HN) a obsluhující sítí (SN). HN vygeneruje očekávanou odpověď (XRES) a její hash (HXRES). Do SN odešle HXRES, nikoli XRES. SN potřebuje pouze porovnat přijatý HRES s HXRES. Tento návrh zabraňuje SN naučit se otevřený RES/XRES, což přidává další vrstvu zabezpečení a ochrany soukromí a omezuje množství citlivých autentizačních dat vystavených navštíveným sítím. HRES je tedy klíčovým prvkem umožňujícím vylepšené funkce ochrany soukromí v 5G, který řeší dvojí problém bezpečné autentizace a nesledovatelnosti účastníka standardizovaným a interoperabilním způsobem.

## Klíčové vlastnosti

- 128bitový kryptografický hash autentizační odpovědi (RES) generované USIM
- Klíčový výstup procedur 5G AKA a EPS AKA pro autentizaci účastníka
- Přenášený vzduchem namísto otevřeného RES za účelem zvýšení ochrany soukromí účastníka
- Vypočítaný mobilním zařízením (ME) pomocí standardizované hashovací funkce (např. SHA-256)
- Ověřený obsluhující sítí proti HXRES přijatému od domovské sítě
- Úspěšné ověření dokazuje držení sdíleného tajného klíče (K) UE a umožňuje následné odvozování klíčů

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps

---

📖 **Anglický originál a plná specifikace:** [HRES na 3GPP Explorer](https://3gpp-explorer.com/glossary/hres/)
