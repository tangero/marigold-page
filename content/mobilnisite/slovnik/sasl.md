---
slug: "sasl"
url: "/mobilnisite/slovnik/sasl/"
type: "slovnik"
title: "SASL – Simple Authentication and Security Layer"
date: 2025-01-01
abbr: "SASL"
fullName: "Simple Authentication and Security Layer"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sasl/"
summary: "Rámec pro přidávání autentizace a volitelných bezpečnostních vrstev k protokolům založeným na spojení. Poskytuje strukturovanou metodu pro vyjednávání a používání autentizačních mechanismů, což umožňu"
---

SASL je rámec pro přidávání autentizace a volitelných bezpečnostních vrstev k protokolům založeným na spojení prostřednictvím vyjednávání mechanismů pro zabezpečenou komunikaci klient-server v sítích 3GPP.

## Popis

Simple Authentication and Security Layer (SASL) je standardizovaný rámec definovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP pro umožnění modulárních (zásuvných) autentizačních mechanismů v rámci spojově orientovaných protokolů. Funguje tak, že přidává vrstvu vyjednávání mezi aplikační protokol a jeho spojení, což umožňuje komunikujícím stranám dohodnout se na vzájemně podporovaném autentizačním mechanismu ze seznamu dostupných možností. Toto vyjednávání je transparentní pro samotný aplikační protokol, který vidí pouze úspěšné navázání autentizovaného (a potenciálně zabezpečeného) sezení. V kontextu 3GPP je SASL primárně specifikováno v TS 33.980 pro použití v IP Multimedia Subsystem (IMS) a dalších síťových funkcích využívajících protokoly jako [SIP](/mobilnisite/slovnik/sip/), [XCAP](/mobilnisite/slovnik/xcap/) nebo [HTTP](/mobilnisite/slovnik/http/), kde usnadňuje zabezpečený přístup ke službám.

Z architektonického hlediska SASL zavádí koncept mechanismu – konkrétní autentizační metody, jako jsou DIGEST-MD5, GSSAPI nebo PLAIN. Při zahájení sezení server klientovi nabídne své podporované mechanismy. Klient poté jeden vybere a zahájí sérii výzev a odpovědí definovaných tímto konkrétním mechanismem. Tyto výměny probíhají v rámci stávajících obálek zpráv protokolu. Klíčové je, že SASL může také vyjednat volitelnou bezpečnostní vrstvu pro ochranu integrity a/nebo důvěrnosti následující datové relace, což je významné vylepšení oproti jednoduchým schématům pouze pro autentizaci.

V sítích 3GPP je úlohou SASL oddělení autentizační logiky od logiky aplikačního protokolu, což podporuje konzistenci a flexibilitu zabezpečení. Například v IMS by uživatelské zařízení (UE) přistupující k serveru [XML](/mobilnisite/slovnik/xml/) Configuration Access Protocol (XCAP) pro správu nastavení doplňkových služeb použilo SASL k autentizaci, typicky pomocí přihlašovacích údajů odvozených z procedury IMS Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Rámec zajišťuje, že i když se vyvíjejí nové, silnější autentizační mechanismy (např. přechod od hashů založených na MD5 k hashům založeným na [SHA](/mobilnisite/slovnik/sha/)), mohou být integrovány bez přepracování základních zásobníků protokolů XCAP nebo SIP. Tato modularita je základním kamenem pro udržení dlouhodobého zabezpečení v rozvíjejících se sítích.

## K čemu slouží

SASL bylo vytvořeno k řešení opakujícího se problému návrhu autentizačních a bezpečnostních funkcí znovu pro každý aplikační protokol. Před rámci jako je SASL si protokoly jako [SMTP](/mobilnisite/slovnik/smtp/), IMAP nebo LDAP každý vyvíjely své vlastní ad-hoc a často slabé autentizační metody, což vedlo k bezpečnostním nekonzistencím, duplikaci úsilí a obtížím při zvyšování kryptografické síly. Primární motivací pro jeho přijetí v 3GPP, zejména pro služby související s IMS, bylo poskytnout standardizovanou, robustní a rozšiřitelnou metodu pro autentizaci uživatelů a aplikací přistupujících k IP službám. Umožňuje opakované použití silných autentizačních přihlašovacích údajů (jako jsou ty z modulu Universal Subscriber Identity Module) napříč různými servisními rozhraními.

Historický kontext jeho zařazení do 3GPP Rel-8 odpovídá plnému nasazení All-IP jádrové sítě a IMS. Jak se služby přesouvaly na IP, potřeba společného autentizačního rámce pro různé aplikační servery se stala klíčovou. SASL řešilo omezení předchozích, často proprietárních nebo protokolově specifických autentizačních schémat tím, že nabídlo neutrální přístup standardizovaný IETF. Řeší problém 'přidávaného' zabezpečení integrací autentizace jako vyjednávané funkce fáze navazování spojení, což zajišťuje, že zabezpečení není dodatečným dojmem, ale základní součástí protokolu pro přístup ke službě. To bylo zásadní pro umožnění zabezpečeného přístupu aplikací třetích stran a pro splnění regulatorních a uživatelských očekávání týkajících se soukromí a ochrany dat v multimediálních službách.

## Klíčové vlastnosti

- Vyjednávání modulárních (zásuvných) autentizačních mechanismů
- Podpora volitelné bezpečnostní vrstvy relace (integrita/důvěrnost)
- Transparentní provoz vůči protokolu
- Opětovné použití přihlašovacích údajů IMS AKA pro autentizaci služby
- Rámec pro přidávání nových kryptografických mechanismů
- Výběr mechanismu klientem ze seznamu nabízeného serverem

## Související pojmy

- [XCAP – XML Configuration Access Protocol](/mobilnisite/slovnik/xcap/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)

## Definující specifikace

- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [SASL na 3GPP Explorer](https://3gpp-explorer.com/glossary/sasl/)
