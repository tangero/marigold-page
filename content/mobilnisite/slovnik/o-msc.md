---
slug: "o-msc"
url: "/mobilnisite/slovnik/o-msc/"
type: "slovnik"
title: "O-MSC – Originating Mobile Switching Centre"
date: 2025-01-01
abbr: "O-MSC"
fullName: "Originating Mobile Switching Centre"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/o-msc/"
summary: "Ústředna mobilního přepojování (MSC), která zajišťuje funkce řízení hovoru a přepojování pro hovor iniciovaný z mobilní sítě. Je první MSC v přenosové cestě hovoru a odpovídá za vytvoření spojení od v"
---

O-MSC je ústředna mobilního přepojování (Mobile Switching Centre), která zajišťuje řízení hovoru a přepojování pro hovor iniciovaný z mobilní sítě. Vytváří spojení od volajícího účastníka a je první MSC v přenosové cestě hovoru.

## Popis

Ústředna [MSC](/mobilnisite/slovnik/msc/) pro volajícího (O-MSC) je entita definovaná v jádru sítě (core network) v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně sítí 2G (GSM) a 3G (UMTS). Jejím hlavním úkolem je řídit navázání hovoru iniciovaného z mobilní sítě. Když uživatelské zařízení (UE) zahájí hlasový hovor, rádiová přístupová síť (RAN) směruje požadavek na navázání hovoru k obsluhující MSC. Pokud tato MSC jako první přijme hovor od volajícího účastníka, přebírá roli O-MSC. O-MSC vykonává klíčové funkce včetně autentizace účastníka, analýzy směrování hovoru a zahájení účtování. Komunikuje s domovským registrem polohy ([HLR](/mobilnisite/slovnik/hlr/)) nebo serverem domovských účastníků ([HSS](/mobilnisite/slovnik/hss/)) pro získání profilu služeb účastníka a s registrem polohy návštěvníka ([VLR](/mobilnisite/slovnik/vlr/)) pro dočasná účastnická data. Na základě volaného čísla O-MSC určí směrovací cestu, což může zahrnovat dotazování na další síťové prvky nebo směrování hovoru k jiné MSC (tzv. Terminating MSC, [T-MSC](/mobilnisite/slovnik/t-msc/)), k bránové MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) pro propojení s jinými sítěmi, nebo k servisnímu uzlu, jako je server hlasové pošty.

Z architektonického hlediska je O-MSC standardní MSC, která přebírá specifickou funkční roli na základě toku hovoru. Ve specifikacích 3GPP je rozdíl mezi O-MSC, T-MSC (Terminating MSC) a GMSC logický, nikoli fyzický; jedna hardwarová platforma MSC může plnit kteroukoli z těchto rolí v závislosti na scénáři hovoru. O-MSC odpovídá za alokaci potřebných zdrojů, jako je okruh na propojení mezi MSC nebo směrem k GMSC, a za aplikaci služeb pro volajícího, k nimž je uživatel přihlášen, jako je zákaz volání nebo bezpodmínečné přesměrování hovoru. Generuje záznamy o hovorech ([CDR](/mobilnisite/slovnik/cdr/)) pro účely účtování, čímž označuje začátek hovoru z pohledu volající strany.

Její činnost je klíčová pro principy inteligentní sítě (IN) používané v mobilních sítích. O-MSC obsahuje funkci přepojování služeb (SSF), která detekuje spouštěcí body pro služby založené na IN (jako jsou předplacené služby nebo bezplatná čísla) a komunikuje s bodem řízení služeb (SCP) prostřednictvím protokolu CAMEL (Customised Applications for Mobile network Enhanced Logic) za účelem provedení složité servisní logiky. Role O-MSC končí, jakmile je hovor přijat a je vytvořena hovorová cesta, přičemž O-MSC zůstává v přenosové cestě po celou dobu hovoru, aby zajišťovala služby během hovoru, doplňkové služby (jako je přidržení hovoru) a procedury ukončení hovoru.

## K čemu slouží

Koncept O-MSC existuje proto, aby poskytl jasný funkční a architektonický referenční bod v rámci sekvence řízení hovoru v okruhově přepínaných mobilních sítích. Před standardizovanými buněčnými systémy bylo telefonní přepojování méně definováno z hlediska rolí pro iniciované a přijímané hovory. Architektura 3GPP tyto role formalizovala, aby umožnila přesné směrování, účtování a vyvolávání služeb. Definice O-MSC umožňuje jednoznačnou aplikaci politik na straně volajícího, jako je autentizace účastníka při zahájení hovoru, aplikace zákazu volání a správné účtování volajícímu. Řeší problém určení místa v potenciálně složité síti MSC, odkud hovor pochází, pro účely legálního odposlechu, fakturace a provádění servisní logiky.

Historicky, jak se GSM vyvíjelo ze základní telefonní služby na platformu pro pokročilé služby inteligentní sítě, stala se potřeba ukotvit servisní logiku k místu vzniku hovoru klíčovou. Například služba předplacených hovorů musí zkontrolovat stav účtu volajícího již na samém začátku pokusu o hovor. O-MSC slouží jako tento ukotvovací bod. Její definice také usnadňuje interoperabilitu sítí a roaming. Když je účastník v roamingu, MSC navštívené sítě slouží jako O-MSC, ale musí komunikovat s HLR/SCP domovské sítě, aby autentizovala uživatele a zkontrolovala služby. Toto jasné oddělení rolí zajišťuje konzistentní zpracování roamingových hovorů, přičemž záznamy o účtování generované O-MSC v navštívené síti jsou odesílány do domovské sítě pro konsolidaci fakturace.

## Klíčové vlastnosti

- Ukotvuje řízení hovoru pro relace iniciované z mobilní sítě
- Provádí počáteční autentizaci účastníka a autorizaci služeb
- Zahajuje generování záznamů o hovorech (CDR) pro účtování volající straně
- Komunikuje s HLR/HSS a VLR pro získání účastnických dat a profilů služeb
- Obsahuje funkci přepojování služeb (SSF) pro služby inteligentní sítě založené na CAMEL
- Určuje směrování hovoru na základě volaných číslic a aplikuje služby pro volajícího (např. zákaz volání)

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [T-MSC – Terminating MSC](/mobilnisite/slovnik/t-msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [O-MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-msc/)
