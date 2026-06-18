---
slug: "wdp"
url: "/mobilnisite/slovnik/wdp/"
type: "slovnik"
title: "WDP – Wireless Datagram Protocol"
date: 2025-01-01
abbr: "WDP"
fullName: "Wireless Datagram Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wdp/"
summary: "WDP je transportní protokol v architektuře WAP, který poskytuje jednotnou datagramovou službu přes různá podkladová bezdrátová přenosová média. Přizpůsobuje se různým síťovým technologiím (jako GSM SM"
---

WDP (Wireless Datagram Protocol) je bezdrátový datagramový protokol, který v architektuře WAP poskytuje jednotnou službu datagramů na transportní vrstvě napříč různými podkladovými bezdrátovými přenosovými médii.

## Popis

Wireless Datagram Protocol (WDP) funguje jako transportní vrstva ve stohu Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)) a je definován tak, aby nabízel nespojované, nespolehlivé datagramové služby podobné [UDP](/mobilnisite/slovnik/udp/), ale uzpůsobené pro bezdrátové sítě. Jeho hlavní funkcí je poskytovat jednotné rozhraní pro přenos dat vyšším vrstvám ([WTP](/mobilnisite/slovnik/wtp/), [WSP](/mobilnisite/slovnik/wsp/)) bez ohledu na vlastnosti podkladové přenosové sítě. WDP toho dosahuje prostřednictvím adaptace na přenosové médium: zahrnuje specifické adaptace pro různé přenosové služby, jako jsou GSM Circuit Switched Data ([CSD](/mobilnisite/slovnik/csd/)), [SMS](/mobilnisite/slovnik/sms/), [USSD](/mobilnisite/slovnik/ussd/), [GPRS](/mobilnisite/slovnik/gprs/), CDMA a další. Každá adaptace mapuje adresování, maximální přenosovou jednotku (MTU) a vlastnosti spolehlivosti nativního média do společných služebních primitiv WDP.

Architektonicky se WDP nachází nad linkovou vrstvou přenosové sítě a pod Wireless Transaction Protocol (WTP). Je zodpovědný za multiplexování a demultiplexování na základě portů, což umožňuje koexistenci více aplikací WAP na jednom zařízení. Adresa WDP se skládá z adresy specifické pro přenosové médium (např. telefonního čísla pro SMS) a čísla portu. Protokol zajišťuje segmentaci a opětovné sestavení, pokud datagram WDP překročí MTU média, přičemž jej rozdělí na pakety specifické pro dané médium pro přenos a na cíli zrekonstruuje. WDP také poskytuje volitelnou detekci chyb prostřednictvím kontrolních součtů, v závislosti na inherentních schopnostech přenosového média.

Při provozu, když aplikace WAP odešle data, vrstva WDP v zařízení přijme datovou část a cílový port od vyšší vrstvy. Konzultuje svou adaptační vrstvu pro přenosové médium, aby naformátovala datagram podle požadavků aktivní sítě, přidá potřebné hlavičky (včetně zdrojového a cílového portu) a předá jej médiu k přenosu. Na přijímací straně je proces obrácený. V rámci 3GPP je WDP odkazován ve specifikacích jako TS 23.057 pro MExE, čímž zajišťuje, že služby WAP mohou být doručovány přes standardizovaná přenosová média 3GPP. Jeho návrh klade důraz na minimální režii a efektivitu, což je klíčové pro omezené bezdrátové spoje raných mobilních datových sítí.

## K čemu slouží

WDP byl vytvořen jako součást sady WAP, aby vyřešil problém interoperability aplikací napříč vysoce fragmentovanou krajinou raných bezdrátových sítí. Různé síťové technologie (GSM, CDMA, iDEN atd.) nabízely velmi odlišné služby přenosu dat s jedinečným adresováním, velikostmi zpráv a charakteristikami spolehlivosti. Vývoj aplikací přímo pro každé přenosové médium byl nepraktický. WDP poskytl abstrakční vrstvu, která tyto rozdíly skryla, a nabídl jednotnou datagramovou službu protokolům WAP vyšších vrstev. To umožnilo vývojářům psát aplikace jednou pro prostředí WAP s jistotou, že budou fungovat napříč více typy přenosových médií.

Řešil omezení používání standardních internetových protokolů, jako je UDP, přímo přes bezdrátová přenosová média, která často měla malé MTU, vysokou chybovost a ne-IP adresování. Začleněním adaptací specifických pro přenosové médium mohl WDP optimálně využít schopnosti každé sítě, například zabalení dat do SMS zpráv nebo použití spojení CSD. Jeho zahrnutí do standardů 3GPP, počínaje Release 4, zajistilo, že UMTS a vyvinuté sítě podporovaly standardizovanou metodu pro přenos WAP, což usnadnilo nasazení mobilních internetových služeb, jako je prohlížení a zasílání zpráv, napříč globálními sítěmi operátorů. WDP byl klíčový pro umožnění první vlny mobilních datových služeb před úplnou IP konvergencí v pozdějších vydáních 3GPP.

## Klíčové vlastnosti

- Adaptační vrstva pro přenosové médium poskytující jednotnou datagramovou službu přes různé bezdrátové sítě
- Multiplexování na základě portů pro podporu více aplikací na jednom zařízení
- Segmentace a opětovné sestavení pro zvládnutí omezení MTU specifických pro přenosové médium
- Podpora jak spojovaných, tak nespojovaných podkladových přenosových médií
- Volitelná detekce chyb prostřednictvím kontrolních součtů tam, kde médium postrádá inherentní ochranu
- Odlehčená struktura hlaviček pro minimalizaci režie protokolu na omezených spojích

## Související pojmy

- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [WTP – Wireless Transaction Protocol](/mobilnisite/slovnik/wtp/)
- [WSP – Web Service Provider](/mobilnisite/slovnik/wsp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/wdp/)
