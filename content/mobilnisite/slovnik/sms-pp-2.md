---
slug: "sms-pp-2"
url: "/mobilnisite/slovnik/sms-pp-2/"
type: "slovnik"
title: "SMS/PP – Short Message Service/Point-to-Point"
date: 2025-01-01
abbr: "SMS/PP"
fullName: "Short Message Service/Point-to-Point"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sms-pp-2/"
summary: "SMS/PP byl původní termín 3GPP pro službu krátkých textových zpráv typu point-to-point, v podstatě synonymní s SMS-PP. Odkazoval na základní službu odesílání textové zprávy od jednoho konkrétního účas"
---

SMS/PP je původní termín 3GPP pro základní službu krátkých textových zpráv typu point-to-point, která odesílá text od jednoho konkrétního účastníka k druhému.

## Popis

[SMS](/mobilnisite/slovnik/sms/)/[PP](/mobilnisite/slovnik/pp/) (Short Message Service/Point-to-Point) je historický termín používaný v raných specifikacích 3GPP, zejména ve vydáních 5 a 6, pro označení přenosové služby pro službu krátkých textových zpráv typu point-to-point. Ve své podstatě je funkčně identický s tím, co pozdější vydání důsledněji označují jako [SMS-PP](/mobilnisite/slovnik/sms-pp/) (Short Message Service – Point to Point). Architektura služby a její provoz popsaný pod SMS/PP sledoval stejné principy: mechanismus store-and-forward využívající síťové služební centrum ([SMS-SC](/mobilnisite/slovnik/sms-sc/)) pro přenos zpráv mezi dvěma mobilními uživateli.

Technický provoz zahrnoval stejné klíčové síťové prvky: mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), obsluhující síťový uzel ([MSC](/mobilnisite/slovnik/msc/) pro okruhově spínanou doménu, [SGSN](/mobilnisite/slovnik/sgsn/) pro paketově spínanou doménu), Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Short Message Service Centre (SMS-SC). MS odeslala zprávu (Mobile Originated) do sítě, která ji směrovala do SMS-SC. SMS-SC následně dotazovala HLR, aby našla aktuální obsluhující uzel příjemce, a přeposlala zprávu k doručení (Mobile Terminated). Použité protokoly byly stejné, zásobník RP-CP-TP přenášený signalizačními kanály.

Rozlišení pomocí přípony "/PP" sloužilo primárně k odlišení této konkrétní služby zasílání zpráv mezi osobami (nebo zařízeními) od jiných potenciálních služeb souvisejících se SMS, jako je rozhlasové vysílání do buněk (SMS-CB) nebo zasílání zpráv do/z externích aplikací. Zápis s lomítkem byl stylistickou volbou v určitých specifikačních dokumentech. Jak se terminologie 3GPP vyvíjela a ustalovala, forma s pomlčkou "SMS-PP" se stala standardizovaným a trvalým termínem používaným ve všech následujících technických specifikacích a popisech architektury, což vedlo k postupnému vyřazení varianty "SMS/PP".

## K čemu slouží

Termín SMS/PP sloužil k explicitní identifikaci varianty point-to-point služby krátkých textových zpráv ve formálním slovníku specifikací 3GPP během počátečních fází standardizace 3G. Když 3GPP převzala vývoj služeb GSM do UMTS, vznikla potřeba formálně kategorizovat a definovat různé typy služeb SMS v rámci nového architektonického rámce.

Reagoval na potřebu srozumitelnosti v raných specifikačních dokumentech, aby se odlišila široce používaná služba zasílání textových zpráv mezi účastníky od jiných, méně běžných režimů SMS. Deskriptor "Point-to-Point" byl klíčový pro specifikaci adresované, směrované povahy služby na rozdíl od služeb vysílání. Motivací pro následné sjednocení terminologie na "SMS-PP" bylo pravděpodobně úsilí o konzistentní konvence pojmenování napříč tisíci stránkami specifikací, odklon od zápisu s lomítkem, který mohl být v určitých kontextech (např. cesty k souborům, vzorce) nejednoznačný, k robustnějšímu složenému termínu s pomlčkou.

## Klíčové vlastnosti

- Identické s SMS-PP: Přenos zpráv typu point-to-point mezi dvěma účastníky
- Závislost na SMS-SC pro směrování typu store-and-forward
- Použití protokolů MAP pro síťovou komunikaci
- Podpora potvrzení o doručení
- Provoz v okruhově spínané i paketově spínané doméně
- Základ pro textovou komunikaci mezi uživateli

## Související pojmy

- [SMS-PP – Short Message Service – Point to Point](/mobilnisite/slovnik/sms-pp/)
- [SMS-SC – Short Message Service - Service Centre](/mobilnisite/slovnik/sms-sc/)
- [SMS-CB – Short Message Service – Cell Broadcast](/mobilnisite/slovnik/sms-cb/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [SMS/PP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sms-pp-2/)
