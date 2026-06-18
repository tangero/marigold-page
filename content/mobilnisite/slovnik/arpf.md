---
slug: "arpf"
url: "/mobilnisite/slovnik/arpf/"
type: "slovnik"
title: "ARPF – Authentication credential Repository and Processing Function"
date: 2026-01-01
abbr: "ARPF"
fullName: "Authentication credential Repository and Processing Function"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/arpf/"
summary: "ARPF je kritická bezpečnostní funkce 5G, která bezpečně ukládá a zpracovává přihlašovací údaje, jako jsou dlouhodobé klíče. Provádí kryptografické operace pro autentizaci a odvození klíčů a tvoří zákl"
---

ARPF je funkce jádra sítě 5G, která bezpečně ukládá přihlašovací údaje účastníka a provádí kryptografické operace potřebné pro autentizaci a odvození klíčů.

## Popis

Authentication credential Repository and Processing Function (ARPF, funkce pro úložiště a zpracování přihlašovacích údajů) je základní bezpečnostní komponenta v architektuře Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) jádra sítě 5G. Slouží jako zabezpečené úložiště pro přihlašovací údaje účastníka, především dlouhodobý tajný klíč (K) a přidružený identifikátor předplatného ([SUPI](/mobilnisite/slovnik/supi/)). Primární úlohou ARPF je provádění kryptografických algoritmů vyžadovaných pro procedury 5G Authentication and Key Agreement (5G-AKA) a EAP-AKA'. Při zahájení autentizační žádosti AUSF/UDM vyvolá ARPF pro vygenerování autentizačních vektorů, které zahrnují náhodné výzvy ([RAND](/mobilnisite/slovnik/rand/)), autentizační tokeny sítě ([AUTN](/mobilnisite/slovnik/autn/)), očekávané odpovědi ([XRES](/mobilnisite/slovnik/xres/)*) a kotvící klíč (K_AUSF), ze kterého jsou odvozeny všechny následné relakční klíče.

Architektonicky ARPF není samostatná síťová funkce ([NF](/mobilnisite/slovnik/nf/)), ale je logicky integrována v rámci UDM pro ukládání přihlašovacích údajů a v rámci AUSF pro zpracování autentizačních vektorů, jak je definováno v 3GPP TS 33.501. Toto oddělení odpovídá principu servisně orientované architektury, kde UDM spravuje data předplatného a AUSF zpracovává autentizační procedury. ARPF s těmito funkcemi komunikuje interně prostřednictvím servisně orientovaných rozhraní. Ukládá přihlašovací údaje podle předplatného, typicky indexované pomocí Subscription Permanent Identifier (SUPI), a podporuje autentizační politiky domovské sítě. Její zpracování zahrnuje provádění sady algoritmů Milenage nebo TUAK pro vygenerování kvintetu (RAND, XRES*, AUTN, K_AUSF) pro 5G-AKA.

Činnost ARPF je spuštěna během počáteční registrace nebo reautentizace. Po obdržení žádosti od AUSF (pro 5G-AKA) nebo přímo od UDM (pro EAP-AKA') ARPF načte dlouhodobý klíč účastníka (K) a SUPI. Poté vygeneruje náhodnou výzvu (RAND) a vypočítá AUTN, který zahrnuje pořadové číslo ([SQN](/mobilnisite/slovnik/sqn/)) a kód autentizace zprávy (MAC) pro autentizaci sítě vůči UE. Současně vypočítá očekávanou odpověď (XRES*) a kotvící klíč K_AUSF. Tyto výstupy tvoří autentizační vektor odeslaný do AUSF, který přeposílá relevantní části do UE prostřednictvím obslužné sítě. UE provede identické výpočty; pokud se její odpověď (RES*) shoduje s XRES*, autentizace uspěje a obě strany odvodí stejný K_AUSF pro následné odvození hierarchie klíčů.

Klíčové součásti funkčnosti ARPF zahrnují databázi přihlašovacích údajů (ukládající K a SUPI), kryptografický algoritmický engine (Milenage/TUAK) a modul pro vynucování politiky pro výběr autentizační metody. Její role přesahuje pouhé ukládání – zajišťuje, že dlouhodobý klíč nikdy neopustí zabezpečený perimetr, čímž zmírňuje rizika expozice klíče. ARPF také podporuje detekci desynchronizace předplatného správou synchronizace SQN, čímž zabraňuje útokům opakováním. V roamingu sídlí ARPF v domovské síti, což umožňuje domovskému operátorovi zachovat kontrolu nad přihlašovacími údaji, zatímco obslužná síť zpracovává přístupové procedury, což ve srovnání s předchozími generacemi zvyšuje bezpečnost a soukromí.

ARPF je ústřední pro vylepšený bezpečnostní rámec 5G, umožňuje funkce jako soukromí předplatného (skrytí SUCI), zabezpečení servisně orientované architektury a izolaci síťového řezání. Centralizací zpracování přihlašovacích údajů poskytuje konzistentní autentizační mechanismus napříč přístupovými technologiemi (3GPP i non-3GPP). Její návrh podporuje regulatorní požadavky na zabezpečené zacházení s přihlašovacími údaji a usnadňuje budoucí upgrady autentizačních metod bez dopadu na ostatní síťové funkce, čímž zajišťuje dlouhodobost a přizpůsobivost v měnícím se prostředí hrozeb.

## K čemu slouží

ARPF byla zavedena v 5G (Release 15) k řešení kritických bezpečnostních nedostatků předchozích generací mobilních sítí, zejména zranitelností v autentizačních systémech 3G a 4G. V 2G/3G/4G byly přihlašovací údaje často uloženy v Home Subscriber Server (HSS) s méně podrobným kryptografickým zpracováním a odvození klíčů bylo někdy distribuováno napříč síťovými elementy, což zvyšovalo rizika expozice. Absence vyhrazeného, funkčně specifického procesoru přihlašovacích údajů ztěžoval implementaci robustního oddělení klíčů a vylepšení ochrany soukromí. Požadavek 5G na silnější ochranu identity účastníka (prostřednictvím SUCI), podpora síťového řezání (vyžadující izolované autentizační kontexty) a integrace s non-3GPP přístupem (např. Wi-Fi) si vyžádaly sofistikovanější a centralizovaný přístup ke správě přihlašovacích údajů.

Primární problém, který ARPF řeší, je zabezpečená izolace a zpracování dlouhodobých autentizačních klíčů. Zapouzdřením ukládání přihlašovacích údajů a kryptografických operací do definované logické funkce zabraňuje úniku klíčů přes síťová rozhraní a snižuje prostor pro útok. To je obzvláště důležité v servisně orientované architektuře 5G, kde síťové funkce komunikují prostřednictvím API založených na HTTP/2 – centralizace citlivých operací v ARPF minimalizuje riziko expozice přihlašovacích údajů během autentizační signalizace. Dále ARPF umožňuje, aby byl bezpečnostní kotvící prvek 5G, K_AUSF, odvozen v kontrolovaném prostředí, čímž zajišťuje, že dlouhodobý klíč (K) není nikdy přenášen ani přímo použit pro ochranu relace, a tím zvyšuje dopřednou utajenost a robustnost hierarchie klíčů.

Historicky autentizace v 4G LTE zahrnovala generování autentizačních vektorů (AV) HSS, které obsahovaly více klíčů, z nichž některé byly odesílány do MME a eNodeB, čímž vznikaly potenciální body pro zachycení. Vytvoření ARPF bylo motivováno potřebou tento proces zefektivnit a zároveň zlepšit bezpečnost. Podporuje model autentizace řízené domovskou sítí v 5G, kde domovská síť (prostřednictvím ARPF) vždy generuje autentizační vektory, a to i v roamingu, čímž zajišťuje konzistentní bezpečnostní politiky. Tím se řeší omezení, jako byl nedostatek autentizace domovskou sítí v některých nastaveních roamingu 4G. ARPF také usnadňuje zavedení nových autentizačních metod (např. EAP-TLS pro IoT) tím, že poskytuje modulární rámec pro zpracování přihlašovacích údajů, což zajišťuje budoucí odolnost sítě vůči vyvíjejícím se hrozbám a regulatorním požadavkům na zvýšené soukromí a ochranu dat.

## Klíčové vlastnosti

- Zabezpečené ukládání dlouhodobého autentizačního klíče účastníka (K) a SUPI
- Kryptografické generování autentizačních vektorů pro procedury 5G-AKA a EAP-AKA'
- Provádění sad algoritmů Milenage nebo TUAK pro autentizaci a odvození klíčů
- Kontrola domovské sítě nad přihlašovacími údaji v roamingu
- Podpora ochrany soukromí předplatného prostřednictvím zahájení autentizace založené na SUCI
- Správa synchronizace pořadového čísla (SQN) k zabránění útoků opakováním

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.514** (Rel-20) — 5G Security Assurance for UDM
- **TR 33.741** (Rel-18) — Home Network Triggered Authentication
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps

---

📖 **Anglický originál a plná specifikace:** [ARPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/arpf/)
