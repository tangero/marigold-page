---
slug: "xmac-a"
url: "/mobilnisite/slovnik/xmac-a/"
type: "slovnik"
title: "XMAC-A – Expected Message Authentication Code for Authentication"
date: 2025-01-01
abbr: "XMAC-A"
fullName: "Expected Message Authentication Code for Authentication"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/xmac-a/"
summary: "XMAC-A je bezpečnostní hodnota vypočítaná během procedury EPS Authentication and Key Agreement (AKA). UE vypočítá XMAC-A a porovná ji s hodnotou MAC-A přijatou ze sítě v rámci autentizačního tokenu (A"
---

XMAC-A je očekávaný kód autentizace zprávy vypočítaný uživatelským zařízením (UE) během EPS AKA za účelem ověření MAC-A sítě, čímž se autentizuje legitimní síť operátora.

## Popis

XMAC-A (Expected [MAC](/mobilnisite/slovnik/mac/) for Authentication) je klíčový parametr v protokolu Evolved Packet System (EPS) Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), používaném v sítích 4G LTE a 5G [NSA](/mobilnisite/slovnik/nsa/)/[SA](/mobilnisite/slovnik/sa/). Generuje jej uživatelské zařízení (UE), konkrétně v jeho zabezpečeném modulu (jako je [USIM](/mobilnisite/slovnik/usim/) nebo podobný prvek odolný proti neoprávněné manipulaci), během procedury primární autentizace. Když UE přijme autentizační požadavek od Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), obsahuje náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)) a autentizační token (AUTN).

Výpočet XMAC-A využívá kryptografický algoritmus, například sadu MILENAGE standardizovanou 3GPP. UE použije svůj dlouhodobý sdílený tajný klíč (K), který je bezpečně uložen a znají jej pouze UE a Authentication Centre (AuC) jeho domovské sítě, spolu s přijatým RAND a Sequence Number (SQN) extrahovaným z AUTN. Tyto prvky se vloží do funkce pro generování MAC (f1). Výstupem tohoto výpočtu je XMAC-A. Kritickou bezpečnostní akcí je porovnání: UE parsuje AUTN, aby získalo MAC-A poskytnuté sítí, a porovná jej bajt po bajtu s lokálně vypočítaným XMAC-A. Pokud jsou shodné, UE kryptograficky ověřilo, že autentizační požadavek pochází od síťové entity, která disponuje správným tajným klíčem K, čímž se síť autentizuje.

Tento proces představuje uživatelskou stranu obousměrné autentizační výměny v EPS AKA. Síť autentizuje uživatele porovnáním přijaté odpovědi (RES) s očekávanou odpovědí (XRES). Naopak, uživatel autentizuje síť prostřednictvím kontroly XMAC-A/MAC-A. Toto obousměrné handshake je zásadní pro model důvěry v sítích 4G/5G a brání útokům typu impersonation. Celý výpočet a porovnání jsou navrženy tak, aby probíhaly v zabezpečeném prostředí (např. na UICC/USIM), a chránily tak tajný klíč K před potenciálním kompromitováním softwarem na hlavním procesoru zařízení.

Specifikace TS 33.105 podrobně popisuje bezpečnostní algoritmy, včetně matematické definice funkcí používaných pro výpočet XMAC-A. Zajišťuje algoritmickou interoperabilitu mezi všemi UE a síťovými AuC globálně. Robustnost tohoto mechanismu podporuje počáteční proceduru připojení a zajišťuje, že UE odvodí následné relací klíče (CK, IK, Kasme) a pokračuje v registraci až poté, co potvrdí, že komunikuje s platnou sítí autorizovanou jeho domovským operátorem.

## K čemu slouží

XMAC-A existuje za účelem poskytnutí obousměrné autentizace v rámci bezpečnostního modelu EPS, což pokračuje a vylepšuje bezpečnostní principy zavedené v 3G UMTS. Jeho primárním účelem je umožnit UE kryptograficky ověřit identitu sítě, ke které se pokouší připojit, a tím vyřešit problém jednostranné autentizace. Bez toho by mohlo být UE oklamáno, aby se připojilo k podvodnému síťovému uzlu, což by vedlo k narušení soukromí, zachycení provozu nebo odmítnutí služby.

Problém, který řeší, je klíčový pro vytvoření důvěry v mobilní síť. V architektuře EPS, kde základní síť (EPC) může zahrnovat roaming mezi více operátory, je zásadní, aby zařízení uživatele potvrdilo, že obsluhující síť (např. navštívená MME) jedná s oprávněním domovské sítě. Ověření XMAC-A tuto jistotu poskytuje tím, že prokazuje, že obsluhující síť disponuje přihlašovacími údaji (odvozenými z K), které mohla poskytnout pouze legitimní domovský operátor.

Jeho vývoj byl motivován potřebou silného, standardizovaného autentizačního mechanismu pro nové Evolved Packet Core (EPC) definované ve 3GPP Release 8. Zatímco je založen na konceptu 3G AKA, EPS AKA a jeho parametr XMAC-A byly specifikovány tak, aby se bezproblémově integrovaly s novými síťovými entitami, jako jsou MME a HSS. Specifikace v TS 33.105 poskytla jasný, algoritmicky agnostický rámec, s MILENAGE jako standardním příkladem, což zajišťuje, že všechny implementace mohou bezpečně interoperovat a tvořit základ pro odvozování klíčů pro NAS a AS zabezpečení.

## Klíčové vlastnosti

- Základní prvek EPS AKA pro autentizaci sítě ze strany UE
- Vypočítán zabezpečeným modulem UE pomocí dlouhodobého klíče K
- Jako vstupy do funkce f1 využívá RAND, SQN a klíč K
- Přímo porovnán s hodnotou MAC-A přijatou v AUTN
- Ověření je předpokladem pro odvození relacích klíčů (CK, IK, Kasme)
- Specifikováno v 3GPP TS 33.105 pro algoritmickou interoperabilitu

## Související pojmy

- [AUTN – Authentication Token](/mobilnisite/slovnik/autn/)
- [MAC-A – Message Authentication Code for Authentication](/mobilnisite/slovnik/mac-a/)
- [SQN – Sequence Number](/mobilnisite/slovnik/sqn/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements

---

📖 **Anglický originál a plná specifikace:** [XMAC-A na 3GPP Explorer](https://3gpp-explorer.com/glossary/xmac-a/)
