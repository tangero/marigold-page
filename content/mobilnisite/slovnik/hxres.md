---
slug: "hxres"
url: "/mobilnisite/slovnik/hxres/"
type: "slovnik"
title: "HXRES – Hash eXpected RESponse"
date: 2026-01-01
abbr: "HXRES"
fullName: "Hash eXpected RESponse"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hxres/"
summary: "Kryptografická hašovací hodnota používaná v procedurách 5G autentizace a dohody o klíči (AKA). Je generována sítí a odeslána UE k ověření pravosti sítě a navázání zabezpečeného spojení. Je klíčovou so"
---

HXRES je kryptografická hašovací hodnota používaná při 5G autentizaci, která umožňuje UE ověřit pravost sítě a navázat zabezpečené spojení.

## Popis

HXRES (Hash eXpected RESponse) je klíčový parametr v protokolu 5G Authentication and Key Agreement (5G [AKA](/mobilnisite/slovnik/aka/)) definovaném v 3GPP TS 33.501. Jedná se o kryptografickou hašovací hodnotu odvozenou z očekávané odpovědi ([XRES](/mobilnisite/slovnik/xres/)*) vygenerované funkcí Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a názvu obsluhující sítě ([SNN](/mobilnisite/slovnik/snn/)). Konkrétně platí HXRES = [KDF](/mobilnisite/slovnik/kdf/)(XRES*, SNN), kde KDF je funkce pro odvození klíče. Tato hodnota je odeslána ze sítě do uživatelského zařízení (UE) jako součást autentizační výzvy během primární autentizační procedury.

Během autentizačního procesu AUSF ve spolupráci s Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) vygeneruje autentizační vektor obsahující několik parametrů, včetně HXRES. Tento vektor je odeslán funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), která předá relevantní výzvu, včetně HXRES, dále do UE. UE nezávisle vypočítá svou vlastní odpověď ([RES](/mobilnisite/slovnik/res/)*) z přijaté výzvy a svých uložených přihlašovacích údajů. Následně spočte haš této hodnoty RES* pomocí stejných parametrů (HRES* = KDF(RES*, SNN)).

UE neodesílá hodnotu RES* zpět do sítě. Místo toho odešle vypočtenou hodnotu HRES* do obsluhující sítě (AMF). AMF poté porovná přijatou hodnotu HRES* od UE s hodnotou HXRES, kterou obdržela od AUSF. Pokud se shodují, dokazuje to, že UE disponuje správným tajným klíčem a úspěšně ověřila výzvu sítě, čímž je potvrzena vzájemná autentizace. Tento mechanismus porovnávání hašovaných hodnot, nikoli nezpracovaných odpovědí, zvyšuje soukromí účastníka tím, že brání obsluhující síti získat nezpracovanou autentizační odpověď, která by mohla být použita ke sledování účastníka napříč různými obsluhujícími sítěmi.

HXRES je zásadní pro cíl architektury 5G zabezpečení poskytnout vylepšenou důvěrnost identity účastníka. Tím, že zajišťuje, aby obsluhující síť viděla pouze hašované hodnoty, omezuje schopnost operátora sítě korelovat autentizační události a sledovat uživatele. Jeho role je těsně propojena s dalšími parametry 5G zabezpečení, jako je SUCI (Subscription Concealed Identifier) a veřejný klíč domovské sítě, a tvoří tak komplexní rámec pro soukromí a autentizaci.

## K čemu slouží

HXRES byl zaveden v 5G (Release 15) k řešení konkrétních nedostatků v oblasti soukromí a zabezpečení identifikovaných v předchozích generacích, zejména v 4G EPS AKA. Ve 4G obsluhující síť přijímala očekávanou odpověď (XRES) v nešifrované podobě od domovské sítě a přímo ji porovnávala s odpovědí (RES) od UE. To znamenalo, že operátor obsluhující sítě měl přístup k jedinečnému, na účastníka specifickému autentizačnímu tokenu, který by potenciálně mohl být použit ke sledování pohybů a aktivit uživatele v síti, což vyvolávalo obavy o soukromí.

Primárním účelem HXRES je zvýšit důvěrnost identity účastníka. Nahrazením přímého porovnání XRES a RES porovnáním jejich hašovaných protějšků (HXRES a HRES*) se obsluhující síť nikdy nedozví nezpracovanou autentizační odpověď. Tento návrh omezuje schopnost obsluhující sítě vytvářet dlouhodobé identifikátory pro sledování. Řeší problém sledování účastníka založeného na obsluhující síti, což je v souladu s přísnějšími předpisy na ochranu osobních údajů, jako je GDPR.

Jeho zavedení bylo dále motivováno potřebou robustnějšího autentizačního rámce vhodného pro různorodou paletu služeb 5G, včetně síťového řezání a masivního IoT. Hašovací mechanismus, vázaný na název obsluhující sítě, také poskytuje vazbu mezi autentizací a konkrétní sítí obsluhující UE, čímž přidává další vrstvu kontextově citlivého zabezpečení. Představuje posun od čisté autentizační kontroly k ověření autentizace chránícímu soukromí.

## Klíčové vlastnosti

- Kryptografický haš očekávané autentizační odpovědi (XRES*).
- Generován funkcí Authentication Server Function (AUSF) domovské sítě.
- Použit pro ověření v obsluhující síti (AMF) bez odhalení nezpracované odpovědi.
- Zvyšuje soukromí účastníka tím, že brání sledování obsluhující sítí.
- Odvozen pomocí funkce pro odvození klíče (KDF) zahrnující Název obsluhující sítě.
- Klíčový parametr v proceduře primární autentizace a dohody o klíči 5G AKA.

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps

---

📖 **Anglický originál a plná specifikace:** [HXRES na 3GPP Explorer](https://3gpp-explorer.com/glossary/hxres/)
