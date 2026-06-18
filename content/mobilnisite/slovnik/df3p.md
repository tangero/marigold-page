---
slug: "df3p"
url: "/mobilnisite/slovnik/df3p/"
type: "slovnik"
title: "DF3P – Delivery Function 3 for GPRS"
date: 2016-01-01
abbr: "DF3P"
fullName: "Delivery Function 3 for GPRS"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/df3p/"
summary: "DF3P je síťová funkce GPRS zodpovědná za doručování krátkých zpráv mobilním zařízením přes paketově spínanou doménu. Umožňuje doručování SMS přes připojení GPRS a představuje alternativu k doručování"
---

DF3P je síťová funkce GPRS zodpovědná za doručování SMS mobilním zařízením přes paketově spínanou doménu a poskytuje alternativu k doručování přes okruhově spínanou doménu.

## Popis

Delivery Function 3 for [GPRS](/mobilnisite/slovnik/gprs/) (DF3P, doručovací funkce 3 pro GPRS) je síťový prvek definovaný ve specifikacích 3GPP, který zajišťuje doručování zpráv služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) přes paketově spínanou síť GPRS. Na rozdíl od tradičního doručování SMS, které využívá okruhově spínanou doménu, DF3P funguje uvnitř paketově spínané jádrové sítě, konkrétně komunikuje s uzlem [SGSN](/mobilnisite/slovnik/sgsn/) (Serving GPRS Support Node) za účelem doručení zpráv mobilním zařízením. Funkce funguje jako zprostředkovatel mezi centrem služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) a sítí GPRS a převádí protokoly pro doručování SMS tak, aby efektivně fungovaly přes paketová připojení.

Z architektonického hlediska je DF3P typicky implementována jako součást SMSC nebo jako samostatný síťový prvek, který komunikuje jak se SMSC, tak s jádrovou sítí GPRS. Se SGSN komunikuje pomocí rozhraní Gd, které přenáší signalizaci specifickou pro SMS a obsah zpráv. Když zpráva SMS dorazí do SMSC a je určena pro mobilní zařízení připojené k GPRS, SMSC ji přepošle do DF3P, která následně iniciuje doručovací procedury přes SGSN. DF3P zvládá všechny potřebné převody protokolů, včetně mapování mezi protokoly SMS a tunelovacími protokoly GPRS.

DF3P funguje tak, že pro každý pokus o doručení SMS naváže logické spojení se SGSN. K identifikaci cílového zařízení používá [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Station International Subscriber Directory Number) nebo [IMSI](/mobilnisite/slovnik/imsi/) (International Mobile Subscriber Identity) a dotazuje se SGSN na aktuální polohu a dostupnost zařízení. Jakmile je zařízení lokalizováno, DF3P zapouzdří zprávu SMS do příslušných protokolů GPRS a přepošle ji do SGSN k doručení mobilnímu zařízení. Funkce také zpracovává potvrzení o doručení, mechanismy opakování pro neúspěšná doručení a ukládání nedoručitelných zpráv podle síťových politik.

Klíčové komponenty DF3P zahrnují modul směrování zpráv, moduly pro převod protokolů, systém sledování stavu doručení a rozhraní k SMSC i SGSN. Modul směrování určuje optimální cestu pro doručení zprávy na základě stavu zařízení a podmínek sítě. Moduly pro převod protokolů překládají mezi protokoly SMS (jako [MAP](/mobilnisite/slovnik/map/) nebo [SMPP](/mobilnisite/slovnik/smpp/)) a protokoly GPRS (včetně GTP a LLC). Systém sledování stavu doručení monitoruje pokusy o doručení zprávy a udržuje potvrzení o doručení pro SMSC. Tyto komponenty spolupracují, aby zajistily spolehlivé doručování SMS přes paketově spínané sítě při zachování kompatibility s existující infrastrukturou SMS.

V širší síťové architektuře hraje DF3P klíčovou roli při umožnění služeb SMS pro zařízení připojená k GPRS, zejména když jsou zařízení v režimu přenosu paketů nebo když nejsou dostupné prostředky okruhově spínané domény. Umožňuje operátorům přesunout provoz SMS z okruhově spínaných sítí na efektivnější paketově spínanou infrastrukturu, čímž zlepšuje využití síťových zdrojů. Funkce také podporuje doručování SMS zařízením, která nemusí mít současně připojení k okruhově i paketově spínané doméně, a zajišťuje tak kontinuitu služby SMS při vývoji sítí směrem k plně IP architekturám.

## K čemu slouží

DF3P byla vytvořena, aby vyřešila problém doručování zpráv SMS mobilním zařízením, která jsou primárně připojena přes paketově spínané sítě GPRS namísto tradičních okruhově spínaných spojení. Před jejím zavedením bylo doručování SMS výhradně závislé na signalizačních kanálech okruhově spínané domény, což se stalo problematickým s vývojem sítí směrem k paketovým architekturám a s tím, jak zařízení trávila více času připojena k paketově spínaným doménám. To vytvářelo mezery ve službách, kdy zprávy SMS nemohly dosáhnout zařízení, která aktivně využívala datové služby GPRS nebo byla přihlášena k paketově spínaným sítím.

Historický kontext vývoje DF3P vychází z přechodu ze sítí 2G na 3G, kde se paketově spínané datové služby stávaly stále důležitějšími. S rostoucí popularitou GPRS a později paketových datových služeb 3G začala mobilní zařízení trávit významný čas připojena k paketově spínaným sítím pro datové aplikace. Tradiční mechanismy doručování SMS nemohly dosáhnout zařízení v těchto stavech, aniž by je nutily přepnout zpět do okruhově spínaného režimu, což přerušovalo datové relace a spotřebovávalo další síťové zdroje. DF3P tento problém vyřešila poskytnutím nativního mechanismu pro doručování SMS přes paketově spínanou doménu.

DF3P řešila několik omezení předchozích přístupů. Za prvé odstranila nutnost, aby se zařízení periodicky přepínala do okruhově spínaného režimu pouze za účelem kontroly zpráv SMS, čímž snížila signalizační režii a zlepšila výdrž baterie. Za druhé umožnila současné poskytování služeb SMS a dat bez přerušení aktivních datových relací. Za třetí poskytla efektivnější mechanismus doručování, který využíval existující paketově spínanou infrastrukturu namísto vyžadování vyhrazených prostředků okruhově spínané domény. Nakonec zajistila budoucí kompatibilitu služeb SMS pro vznikající plně IP síťové architektury, kde byly komponenty okruhově spínané domény nahrazovány paketovými řešeními.

## Klíčové vlastnosti

- Doručování SMS přes paketově spínané sítě GPRS
- Převod protokolů mezi protokoly SMS a GPRS
- Rozhraní se SGSN přes rozhraní Gd
- Sledování stavu doručení a podávání hlášení
- Mechanismy opakování pro neúspěšná doručení zpráv
- Podpora adresování zařízení založeného na MSISDN i IMSI

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)

## Definující specifikace

- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [DF3P na 3GPP Explorer](https://3gpp-explorer.com/glossary/df3p/)
