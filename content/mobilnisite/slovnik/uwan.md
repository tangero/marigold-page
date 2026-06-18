---
slug: "uwan"
url: "/mobilnisite/slovnik/uwan/"
type: "slovnik"
title: "UWAN – Untrusted Wireless Access Network"
date: 2025-01-01
abbr: "UWAN"
fullName: "Untrusted Wireless Access Network"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uwan/"
summary: "Přístupová síť mimo 3GPP (jako je Wi-Fi), které jádrová síť 3GPP nevěří implicitně. Pro bezpečnou integraci takového přístupu jsou spojení uživatelského zařízení (UE) směrována přes rozšířenou bránu p"
---

UWAN je nedůvěryhodná bezdrátová přístupová síť mimo 3GPP, například Wi-Fi, kde musí být uživatelský provoz před dosažením jádra 3GPP zabezpečen prostřednictvím ePDG pomocí tunelu IPsec.

## Popis

Nedůvěryhodná bezdrátová přístupová síť (UWAN) je konceptuální klasifikace v architekturách 3GPP pro Evolved Packet System (EPS) a 5G System (5GS), která označuje jakoukoli bezdrátovou IP přístupovou síť, kterou neprovozuje operátor mobilní sítě nebo která není považována za dostatečně bezpečnou pro přímé, důvěryhodné spojení s jádrem 3GPP. Nejběžnějším příkladem je veřejná nebo privátní Wi-Fi síť (např. [IEEE](/mobilnisite/slovnik/ieee/) 802.11). Základním principem je, že síť 3GPP se nemůže spoléhat na vlastní bezpečnostní mechanismy UWAN pro ochranu provozu uživatelské roviny a signalizace. Proto je jako povinný vstupní bod zavedena speciální bezpečnostní brána, rozšířená brána paketových dat (ePDG).

Když se uživatelské zařízení (UE) připojí k síti přes UWAN, musí nejprve objevit a vybrat vhodný ePDG. UE následně s ePDG vytvoří tunel [IPsec](/mobilnisite/slovnik/ipsec/) (konkrétně tunel založený na IKEv2). Tento tunel zapouzdřuje veškerý provoz určený pro jádrovou síť 3GPP, včetně autentizační signalizace a paketů uživatelských dat. ePDG funguje jako bezpečnostní brána, která ukončuje tunel IPsec z nedůvěryhodné strany a představuje důvěryhodné rozhraní směrem k jádru. Spolupracuje s infrastrukturou 3GPP [AAA](/mobilnisite/slovnik/aaa/) ([HSS](/mobilnisite/slovnik/hss/)/AAA Server) k autentizaci UE pomocí protokolů EAP-AKA nebo EAP-AKA' přes tento zabezpečený tunel. Po autentizaci ePDG nastaví potřebnou konektivitu k bráně paketových dat ([PGW](/mobilnisite/slovnik/pgw/)) v EPS nebo k funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) v 5GS, čímž vytvoří pro UE zabezpečenou end-to-end logickou cestu.

Architektura zahrnuje několik klíčových komponent: UE s podporou IKEv2/IPsec a vyhledávání ePDG (pomocí [DNS](/mobilnisite/slovnik/dns/)), samotnou UWAN, která poskytuje pouze IP konektivitu, ePDG jako hranici důvěry a prvky jádrové sítě (HSS, PGW/UPF). Role ePDG je kritická – ověřuje přihlašovací údaje UE, vynucuje politiky a zajišťuje, že veškerý provoz z nedůvěryhodného přístupu je před vstupem do důvěryhodné domény operátora řádně šifrován a chráněn z hlediska integrity. Tento model umožňuje operátorům bezpečně využívat rozsáhlou stávající infrastrukturu Wi-Fi pro odlehčování dat a kontinuitu služeb, aniž by byla ohrožena bezpečnostní standardy jejich mobilní jádrové sítě.

## K čemu slouží

Koncept UWAN byl formalizován, aby řešil rostoucí potřebu mobilních operátorů integrovat všudypřítomné, ale inherentně nezabezpečené Wi-Fi sítě do své nabídky služeb. Před jeho standardizací byl přístup přes Wi-Fi často řešen jako zcela oddělený, best-effort přístup k internetu bez integrace s buněčnými službami, jako je IMS nebo bezproblémová mobilita. Problém byl dvojí: poskytnout zabezpečený přístup splňující přísné požadavky 3GPP na autentizaci a důvěrnost a umožnit bezproblémovou kontinuitu služeb mezi přístupy 3GPP a mimo 3GPP. Vytvoření architektury UWAN/ePDG ve vydání 8 (EPS) poskytlo standardizované řešení.

Vyřešilo bezpečnostní problém stanovením jasné hranice důvěry. Namísto pokusů o zabezpečení samotného Wi-Fi spoje (což je na veřejných hotspotech často nepraktické) předpokládá nejhorší scénář – přístup je nedůvěryhodný – a nařizuje end-to-end šifrování mezi UE a sítí operátora. To chrání před odposlechem a manipulací na Wi-Fi spoji. Dále umožnilo těsnou integraci s rámcem předplatného a politik jádrové sítě ([PCRF](/mobilnisite/slovnik/pcrf/)/PCF), což operátorům dovoluje aplikovat stejné fakturační, QoS a přístupové politiky bez ohledu na to, zda je uživatel na LTE nebo Wi-Fi. To byl klíčový motivátor pro vytvoření standardizovaného, zabezpečeného rámce pro spolupráci sítě mimo 3GPP, který připravil cestu pro funkce jako Wi-Fi Calling a bezproblémové odlehčování.

## Klíčové vlastnosti

- Klasifikace pro IP přístupové sítě mimo 3GPP, kterým chybí implicitní důvěra (např. veřejné Wi-Fi)
- Ukládá povinné použití ePDG jako zabezpečené brány a hranice důvěry
- Vyžaduje, aby UE vytvořilo s ePDG tunel IPsec/IKEv2 pro veškerý provoz 3GPP
- Pro silnou autentizaci UE přes nedůvěryhodný spoj využívá EAP-AKA/AKA'
- Umožňuje integrované řízení politik a účtování prostřednictvím interakce s PCRF/PCF
- Poskytuje základ pro bezproblémovou mobilitu k/od důvěryhodného přístupu 3GPP

## Související pojmy

- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [UWAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/uwan/)
