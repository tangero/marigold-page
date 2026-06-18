---
slug: "cts-me"
url: "/mobilnisite/slovnik/cts-me/"
type: "slovnik"
title: "CTS-ME – Cellular Text Telephone Modem Mobile Equipment"
date: 2025-01-01
abbr: "CTS-ME"
fullName: "Cellular Text Telephone Modem Mobile Equipment"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cts-me/"
summary: "CTS-ME umožňuje služby textové telefonie pro uživatele se sluchovým a řečovým postižením přes mobilní sítě. Poskytuje komunikaci textem v reálném čase integrací textového telefonního modemu do mobilní"
---

CTS-ME je komponenta mobilního zařízení, která integruje textový telefonní modem pro poskytování služeb komunikace textem v reálném čase přes mobilní sítě uživatelům se sluchovým a řečovým postižením.

## Popis

CTS-ME (Cellular Text Telephone Modem Mobile Equipment) je standardizovaná implementace funkce textové telefonie v mobilních zařízeních, speciálně navržená pro službu uživatelům se sluchovým nebo řečovým postižením. Tato technologie integruje textový telefonní modem přímo do mobilního zařízení, což umožňuje komunikaci textem v reálném čase přes mobilní sítě. Tato implementace dodržuje standard [ITU-T](/mobilnisite/slovnik/itu-t/) V.18 pro textovou telefonii, čímž zajišťuje interoperabilitu s tradičními textovými telefonními zařízeními a službami. Funkce CTS-ME funguje jako služba aplikační vrstvy, která komunikuje s audio zpracováním zařízení a síťovými komunikačními protokoly za účelem navázání textových konverzací.

Z architektonického hlediska se CTS-ME skládá z několika klíčových komponent: implementace textového telefonního modemu, audio zpracovacích modulů pro akustické spojení, zpracování protokolů pro přenos textu a uživatelských rozhraní pro zobrazení a zadávání textu. Modemová komponenta implementuje zásobník protokolů V.18, včetně funkcí modulace/demodulace, kódování/dekódování znaků a mechanismů opravy chyb. Audio zpracovací moduly zajišťují převod mezi digitálními textovými daty a analogovými audio signály, které lze přenášet přes hlasové kanály. Systém komunikuje s mikrofonem a reproduktorem zařízení pro akustické spojení nebo se připojuje přímo k audio subsystému pro elektrické spojení, pokud je dostupné.

Při provozu CTS-ME navazuje hovory textové telefonie pomocí standardních hlasových kanálů mobilní sítě. Když uživatel zahájí hovor textové telefonie, aplikace CTS-ME aktivuje textový telefonní modem a naváže spojení s textovým telefonním zařízením druhé strany. Systém moduluje textové znaky do audio tónů pomocí frekvenční manipulace ([FSK](/mobilnisite/slovnik/fsk/)) nebo jiných modulačních schémat specifikovaných ve V.18. Tyto audio tóny jsou přenášeny přes hlasový kanál jako běžná řeč. Na přijímací straně proces demodulace extrahuje textové znaky z přijatých audio signálů a zobrazí je uživateli. Systém podporuje plně duplexní provoz, což umožňuje současný přenos a příjem textu.

Tato technologie hraje v síti klíčovou roli při poskytování služeb přístupnosti bez nutnosti úprav síťové infrastruktury. Protože CTS-ME funguje přes standardní hlasové kanály, využívá stávající mobilní infrastrukturu a zároveň poskytuje specializované služby pro uživatele s postižením. Implementace zahrnuje funkce pro sestavení a vyjednávání hovoru, kdy si zařízení vyměňují informace o schopnostech, aby určila optimální režim a parametry textové telefonie. CTS-ME také podporuje záložní mechanismy a kompatibilní režimy pro zajištění komunikace s různými typy textových telefonních zařízení, včetně starších zařízení a různých regionálních implementací.

## K čemu slouží

CTS-ME bylo vytvořeno za účelem řešení kritické potřeby dostupných komunikačních služeb pro uživatele se sluchovým a řečovým postižením v mobilních sítích. Před jeho zavedením sloužily mobilní sítě primárně hlasové komunikaci, což vytvářelo významné bariéry pro uživatele, kteří byli závislí na textových komunikačních metodách. Tradiční služby textové telefonie existovaly v pevných sítích, ale nebyly dostupné v mobilním prostředí, takže uživatelé s postižením neměli odpovídající možnosti mobilní komunikace. Tato technologie byla motivována regulatorními požadavky na přístupnost telekomunikací a základním principem univerzální služby, který zajišťuje, že mobilní komunikace prospívá všem segmentům společnosti.

Vývoj CTS-ME vyřešil problém integrace funkce textové telefonie do mobilních zařízení bez nutnosti specializované síťové infrastruktury. Předchozí přístupy vyžadovaly buď samostatná textová telefonní zařízení připojená k mobilním telefonům, nebo spoléhaly na [SMS](/mobilnisite/slovnik/sms/), kterým chyběly charakteristiky konverzace v reálném čase tradiční textové telefonie. CTS-ME poskytlo standardizované řešení, které umožnilo konverzace textem v reálném čase přes hlasové kanály, při zachování známého uživatelského zážitku textové telefonie a využití stávající mobilní infrastruktury. Tento přístup zajistil zpětnou kompatibilitu s existujícími službami a zařízeními textové telefonie a zároveň umožnil mobilní přístupnost.

Historický kontext ukazuje, že CTS-ME vzniklo jako součást širších snah o zpřístupnění telekomunikačních služeb lidem s postižením. Tato technologie byla vyvinuta v souladu s mezinárodními standardy a regulatorními rámci, které nařizují dostupné komunikační služby. Integrací funkce textové telefonie přímo do mobilního zařízení CTS-ME odstranilo potřebu externích adaptérů nebo specializovaných zařízení, čímž se dostupná komunikace stala pohodlnější a široce dostupnější. Řešení řešilo jak technické, tak praktické výzvy a poskytlo robustní implementaci, která fungovala za různých síťových podmínek a typů zařízení při zachování souladu s požadavky na přístupnost.

## Klíčové vlastnosti

- Dodržování standardu V.18 pro textovou telefonii
- Přenos textu v reálném čase přes hlasové kanály
- Podpora akustického a elektrického spojení
- Možnost plně duplexní textové komunikace
- Automatické vyjednávání režimu a záložní mechanismy
- Integrace s audio subsystémy mobilního zařízení

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [CTS-ME na 3GPP Explorer](https://3gpp-explorer.com/glossary/cts-me/)
