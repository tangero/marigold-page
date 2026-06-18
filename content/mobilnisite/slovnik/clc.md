---
slug: "clc"
url: "/mobilnisite/slovnik/clc/"
type: "slovnik"
title: "CLC – Compression Language Context"
date: 2025-01-01
abbr: "CLC"
fullName: "Compression Language Context"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/clc/"
summary: "CLC (Compression Language Context – kontext jazyka pro kompresi) je specifikace 3GPP definující standardizovaný jazyk pro popis kompresních algoritmů a jejich parametrů. Umožňuje efektivní signalizaci"
---

CLC je specifikace 3GPP definující standardizovaný jazyk pro popis kompresních algoritmů a jejich parametrů, který umožňuje efektivní signalizaci a zajišťuje interoperabilitu mezi síťovými prvky.

## Popis

Compression Language Context (CLC – kontext jazyka pro kompresi) je definován ve specifikaci 3GPP 23.042 jako formální jazyk pro popis kompresních algoritmů, jejich parametrů a provozních charakteristik v mobilních sítích. Tento jazyk slouží jako standardizovaná metoda pro síťové prvky ke komunikaci svých kompresních schopností a požadavků během navazování služby a přenosu dat. Rámec CLC poskytuje strukturovanou syntaxi, kterou mohou kompatibilní síťové entity parsovat a interpretovat, což umožňuje dynamické vyjednávání a konfiguraci kompresních parametrů na základě požadavků služby, stavu sítě a schopností zařízení.

Z architektonického hlediska CLC funguje jako mezivrstva mezi aplikačními službami a podkladovými transportními mechanismy. Když služba jako [SMS](/mobilnisite/slovnik/sms/) nebo [MMS](/mobilnisite/slovnik/mms/) vyžaduje kompresi, zdrojová entita vygeneruje popis CLC specifikující kompresní algoritmus (jako Huffmanovo kódování, varianty Lempel-Ziv nebo proprietární schémata), reference na slovníky, kompresní parametry a očekávané výkonnostní charakteristiky. Tento popis je následně přenesen do přijímající entity jako součást signalizace služby nebo v rámci samotných protokolových datových jednotek. Přijímající entita popis CLC zpracuje, ověří specifikovanou kompresní metodu vůči vlastním schopnostem a podle toho nakonfiguruje svůj dekompresní engine.

Klíčovými součástmi systému CLC jsou formát deskriptoru CLC, registr kompresních algoritmů, schémata kódování parametrů a protokoly pro vyjednávání schopností. Formát deskriptoru sleduje hierarchickou strukturu s povinnými a volitelnými prvky, včetně identifikátorů algoritmů, informací o verzi, sad parametrů a ukazatelů výkonu. Registr kompresních algoritmů udržuje standardizované reference na známé kompresní metody, což zajišťuje konzistentní interpretaci napříč různými implementacemi. Schémata kódování parametrů definují, jak jsou specifická nastavení komprese (jako výběr slovníku, úroveň komprese nebo velikost okna) reprezentována v rámci CLC.

Role CLC v síti přesahuje pouhou signalizaci komprese – umožňuje adaptivní kompresní strategie, kde lze na základě typu obsahu, stavu sítě nebo požadavků na kvalitu služby vybírat různé algoritmy. Pro textové služby umožňuje CLC síti optimalizovat přenosovou efektivitu výběrem nejvhodnější kompresní metody pro konkrétní jazyk, znakovou sadu nebo strukturu zprávy. Systém také podporuje progresivní kompresi, kde lze použít více algoritmů sekvenčně, přičemž každý stupeň je popsán vlastním kontextem CLC. Tento vrstvený přístup umožňuje sofistikované kompresní strategie při zachování zpětné kompatibility s jednoduššími implementacemi.

## K čemu slouží

CLC byl vytvořen, aby řešil rostoucí potřebu efektivní komprese dat v raných sítích 3G, zejména pro messagingové služby, které získávaly na popularitě. Před standardizací CLC různí výrobci implementovali proprietární metody signalizace komprese, které byly vzájemně nekompatibilní, což vedlo k problémům s interoperabilitou a suboptimálnímu kompresnímu výkonu. Absence společného jazyka pro popis kompresních schopností znamenala, že sítě často přistupovaly k žádné kompresi nebo k základním standardizovaným schématům, a přicházely tak o příležitosti k optimalizaci šířky pásma.

Historický kontext vývoje CLC spočívá v přechodu od okruhově spínaných služeb k paketově spínaným službám ve verzi 3GPP Release 99. Jak se [SMS](/mobilnisite/slovnik/sms/) vyvíjelo ve služby messagingu s více funkcemi a služby [MMS](/mobilnisite/slovnik/mms/), objem textového a multimediálního obsahu dramaticky rostl, což vytvářelo tlak na dostupné rádiové zdroje. Předchozí přístupy spoléhaly na pevná kompresní schémata pevně zakódovaná v protokolech, která se nedokázala přizpůsobit různým typům obsahu nebo stavům sítě. CLC zavedl flexibilní, rozšiřitelný rámec, který dokázal popsat jakýkoli kompresní algoritmus, což umožnilo sítím vyvíjet své kompresní strategie bez nutnosti změn protokolů.

CLC vyřešil několik klíčových problémů: odstranil vazbu na konkrétního výrobce v oblasti kompresních technologií, umožnil dynamický výběr algoritmu na základě podmínek v reálném čase a poskytl rámec připravený na budoucnost pro nové kompresní metody. Standardizací způsobu komunikace kompresních schopností umožnil CLC sítím implementovat sofistikované kompresní strategie při zachování interoperability mezi různými výrobci zařízení. To bylo obzvláště důležité pro scénáře roamingu, kdy se zařízení účastníka mohlo setkat se sítěmi s různými kompresními schopnostmi.

## Klíčové vlastnosti

- Standardizovaný jazyk pro popis kompresních algoritmů
- Dynamické vyjednávání schopností mezi síťovými prvky
- Podpora více kompresních algoritmů včetně proprietárních schémat
- Hierarchické kódování parametrů pro složité kompresní konfigurace
- Integrace se službami messagingu 3GPP (SMS/MMS)
- Rozšiřitelný rámec pro budoucí kompresní technologie

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/clc/)
