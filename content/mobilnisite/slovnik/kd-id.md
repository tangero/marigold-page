---
slug: "kd-id"
url: "/mobilnisite/slovnik/kd-id/"
type: "slovnik"
title: "KD-ID – Keyword Dictionary Identifier"
date: 2025-01-01
abbr: "KD-ID"
fullName: "Keyword Dictionary Identifier"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/kd-id/"
summary: "KD-ID je jedinečný identifikátor slovníku klíčových slov používaného ve službě krátkých textových zpráv (SMS) 3GPP pro umožnění jazykově nezávislého kódování předdefinovaných frází. Umožňuje sítím a z"
---

KD-ID je jedinečný identifikátor slovníku klíčových slov používaného v SMS službě 3GPP pro umožnění jazykově nezávislého kódování předdefinovaných frází.

## Popis

Identifikátor slovníku klíčových slov (KD-ID) je parametr definovaný v 3GPP TS 23.042, který specifikuje kompresní protokoly pro službu krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)). Jedná se o číselný identifikátor odkazující na konkrétní „slovník klíčových slov“ – standardizovanou vyhledávací tabulku obsahující seznam předdefinovaných slov nebo frází. Tento mechanismus je součástí architektury komprese SMS navržené ke snížení počtu bitů potřebných k přenosu textové zprávy, čímž se zvyšuje kapacita sítě a umožňují se delší zprávy v rámci omezení transportní vrstvy SMS (140 bajtů). Z architektonického hlediska je KD-ID přenášen v rámci protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) komprimované SMS, konkrétně v hlavičce indikace komprese.

Jak to funguje: Odesílatel i příjemce (mobilní stanice nebo SMS servisní centrum) musí mít přístup ke stejnému slovníku, na který KD-ID odkazuje. Když uživatel vytvoří zprávu obsahující fráze přítomné ve slovníku, může zasílací aplikace nebo kompresní funkce sítě nahradit plný textový řetězec krátkým referenčním kódem (indexem do slovníku) spolu s KD-ID. Například místo odeslání bajtů pro „Děkujeme za vaši zprávu“ systém odešle KD-ID pro slovník „Anglické běžné fráze“ a indexové číslo, například 15. Příjemce použije KD-ID k výběru správného slovníku z místního úložiště a pomocí indexu zrekonstruuje původní frázi.

Klíčové komponenty zahrnují samotné slovníky klíčových slov, což jsou standardizované nebo operátorské specifické seznamy, a kompresní/dekompresní enginy v UE a [SMS-SC](/mobilnisite/slovnik/sms-sc/). Role KD-ID je klíčová pro interoperabilitu; zajišťuje, že příjemce použije pro úspěšnou dekompresi úplně stejný slovník jako odesílatel. Slovníky mohou být předinstalovány na kartách [SIM](/mobilnisite/slovnik/sim/)/[USIM](/mobilnisite/slovnik/usim/), vestavěny do firmwaru zařízení nebo případně staženy přes vzdušné rozhraní (over-the-air). Systém podporuje více slovníků (např. pro různé jazyky nebo specializované domény, jako je bankovnictví), každý se svým jedinečným KD-ID. Tato funkce je primárně využívána pro běžné fráze v business-to-consumer zprávách (např. oznámení o doručení, jednorázová hesla) nebo pro překonání jazykových bariér v roamingových scénářích pomocí univerzálního slovníku cestovních pojmů.

## K čemu slouží

KD-ID a související komprese pomocí slovníku klíčových slov byly vyvinuty pro překonání inherentních omezení původní specifikace [SMS](/mobilnisite/slovnik/sms/), která byla založena na 7bitové výchozí GSM abecedě a omezena na 160 znaků na zprávu. S explozivním růstem využití SMS existoval komerční i technický tlak na umístění většího množství informací do jedné segmentové zprávy za účelem snížení nákladů, zlepšení uživatelského zážitku u delších zpráv a šetření signalizační šířky pásma na rádiovém rozhraní. Tradiční textová komprese založená na Huffmanově kódování je u velmi krátkých zpráv méně efektivní, ale nahrazení běžných frází krátkými kódy nabízí významné zisky.

Vytvoření tohoto standardu bylo motivováno potřebou chytré kompresní techniky na sémantické úrovni, která by mohla dosáhnout vysokých kompresních poměrů pro opakující se obsah typický v automatizovaných nebo transakčních zprávách. Řešilo problém odesílání identických frází milionkrát napříč sítí, jako je „Váš zůstatek je“ nebo „Váš kód je“, jejich přeměnou na drobné reference. To bylo obzvláště cenné pro mobilní operátory a poskytovatele služeb odesílající velké objemy podobných oznámení.

Dále řešilo výzvu mezinárodního roamingu a vícejazyčné podpory. Cestující mohl přijmout komprimovanou zprávu s KD-ID pro „Univerzální cestovní slovník“ a jeho telefon ji mohl dekomprimovat do rodného jazyka, pokud jeho lokální slovník měl stejné indexy namapované na přeložené fráze. To otevřelo cestu pro jazykově nezávislé služby zasílání zpráv. Přestože jeho praktické rozšířené nasazení bylo omezeno vzestupem bohatých messagingových aplikací, framework KD-ID zůstává standardizovaným, efektivním řešením pro specifické use case SMS typu machine-to-machine (M2M) a application-to-person ([A2P](/mobilnisite/slovnik/a2p/)), kde jsou šířka pásma a náklady kritickými omezeními.

## Klíčové vlastnosti

- Jedinečný identifikátor pro konkrétní slovník klíčových slov
- Umožňuje vysoký kompresní poměr pro předdefinované textové fráze
- Přenášen v hlavičce kompresního protokolu SMS
- Podporuje více slovníků pro různé jazyky nebo use case
- Usnadňuje jazykově nezávislou výměnu zpráv
- Snižuje signalizační zatížení a zvyšuje efektivní kapacitu SMS

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [SMS-SC – Short Message Service - Service Centre](/mobilnisite/slovnik/sms-sc/)

## Definující specifikace

- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP

---

📖 **Anglický originál a plná specifikace:** [KD-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/kd-id/)
