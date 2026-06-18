---
slug: "df3"
url: "/mobilnisite/slovnik/df3/"
type: "slovnik"
title: "DF3 – Delivery Function 3"
date: 2016-01-01
abbr: "DF3"
fullName: "Delivery Function 3"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/df3/"
summary: "DF3 je standardizovaná doručovací funkce definovaná v 3GPP TS 43.033 pro doručování služby krátkých zpráv (SMS) v sítích GSM/UMTS. Zajišťuje směrování a doručování SMS zpráv mezi centrem služby krátký"
---

DF3 je standardizovaná doručovací funkce v sítích GSM/UMTS, která zajišťuje směrování a doručování SMS zpráv mezi centrem služby krátkých zpráv (SMSC) a mobilní stanicí (MS).

## Popis

Delivery Function 3 (DF3) je klíčová funkční komponenta v architektuře služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) pro sítě GSM a UMTS, standardizovaná v 3GPP TS 43.033. Funguje jako součást mechanismu doručování SMS a je konkrétně odpovědná za poslední úsek doručení mobilně-terminované ([MT](/mobilnisite/slovnik/mt/)) SMS ze střediska služby krátkých zpráv ([SMSC](/mobilnisite/slovnik/smsc/)) k cílové mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). DF3 není samostatný fyzický uzel, ale logická funkce, která může být implementována v rámci síťových prvků, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)). Jejím hlavním úkolem je řídit interakci s mobilním zařízením za účelem dokončení přenosu zprávy.

Architektonicky se DF3 nachází mezi SMSC (přes SMS Gateway MSC, [SMS-GMSC](/mobilnisite/slovnik/sms-gmsc/)) a rádiovou přístupovou sítí. Když SMS-GMSC obdrží zprávu od SMSC, dotazuje se na Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) o směrovací informace k nalezení MSC/VLR příjemce. MSC/VLR, které hostí funkci DF3, se poté pokusí o doručení. DF3 zvládá protokolové interakce s MS přes rádiové rozhraní, řídí specifické signalizační procedury pro přenos SMS, včetně vyvolání (pagingu) MS, pokud je v klidovém režimu, a navázání potřebného dočasného signalizačního spojení.

Funkce pracuje tak, že přijme zprávu SMDPP (Short Message Delivery Point-to-Point) od SMS-GMSC. DF3 poté iniciuje komunikaci s MS pomocí protokolů definovaných pro danou síť (např. DTAP - Direct Transfer Application Part v GSM). Je odpovědná za spolehlivý přenos SMS-TPDU (Transfer Protocol Data Unit) k MS a za přijetí a zpracování hlášení o doručení od MS. Pokud je MS nedostupná (např. vypnutá nebo mimo dosah), DF3 informuje MSC/VLR, které následně upozorní HLR, aby nastavilo příznak čekající zprávy a uložilo adresu obsluhujícího MSC/VLR, což umožní pozdější doručení, když se MS stane dostupnou.

Klíčové komponenty procesu DF3 zahrnují logiku pro zpracování zpráv, rozhraní k řízení rádiových prostředků pro navázání signalizačního spojení a rozhraní k HLR/VLR pro informace o stavu a poloze účastníka. Její role je klíčová pro zajištění principu 'ulož a předej' (store-and-forward) u SMS, poskytuje mechanismy pro opakování pokusů, oznámení o selhání a potvrzení úspěšného doručení. Díky tomu, že jde o standardizovanou funkci, DF3 zajišťuje konzistentní chování doručování SMS napříč různými dodavateli síťového vybavení a mobilními operátory, což bylo zásadní pro globální interoperabilitu služeb SMS.

## K čemu slouží

DF3 byla vytvořena za účelem poskytnutí standardizovaného, spolehlivého mechanismu pro doručování zpráv služby krátkých zpráv (SMS) do mobilních zařízení v sítích GSM a UMTS. Před jejím formálním definováním v 3GPP specifikacích byly metody doručování textových zpráv do mobilů méně ustálené, což mohlo vést k problémům s interoperabilitou mezi různým síťovým vybavením od různých výrobců. Standardizace DF3 jako součásti celkové architektury SMS v TS 43.033 zajistila jednotný postup pro závěrečný krok doručení, což bylo klíčové pro komerční úspěch a spolehlivost SMS jako služby pro masový trh.

Problém, který řeší, je výzva 'poslední míle' při doručování SMS v jádrové síti s přepojováním okruhů. Přesně definuje, jak má síť interagovat s mobilním zařízením při přenosu obsahu zprávy, při řešení dočasných selhání (jako je vypnutý mobil) a při generování hlášení o doručení. Tím se vyřešil problém nekonzistentního chování při doručování zpráv a zlepšil se uživatelský zážitek tím, že se doručování SMS stalo předvídatelným a spolehlivým. Její vytvoření bylo motivováno potřebou přeměnit SMS z technické možnosti na robustní, fakturovatelnou a široce interoperabilní službu.

Historicky byla SMS součástí specifikací GSM Fáze 1, ale její architektura a funkční rozdělení, jako je DF3, byly podrobněji rozpracovány v pozdějších vydáních. Formální definice DF3 v Rel-8 (zdokumentovaná v TS 43.033) poskytla jasný referenční bod pro síťové implementace. Řešila omezení dřívějších, více ad-hoc přístupů specifikací přesných procedur, časovačů a zpracování chyb, což snížilo ztrátu zpráv a zlepšilo úspěšnost doručení ve složitých síťových prostředích s více dodavateli.

## Klíčové vlastnosti

- Standardizovaná logická funkce pro doručování MT-SMS
- Zajišťuje protokolovou interakci s mobilní stanicí (MS) přes rádiové rozhraní
- Řídí procedury opakování doručení při dočasném selhání
- Generuje a zpracovává hlášení o stavu doručení
- Komunikuje s HLR/VLR pro získání informací o poloze a stavu účastníka
- Funguje v rámci MSC/VLR v jádrové síti s přepojováním okruhů

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [SMS-GMSC – Short Message Service Gateway MSC](/mobilnisite/slovnik/sms-gmsc/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [DF3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/df3/)
