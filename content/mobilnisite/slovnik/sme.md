---
slug: "sme"
url: "/mobilnisite/slovnik/sme/"
type: "slovnik"
title: "SME – Short Message Entities"
date: 2025-01-01
abbr: "SME"
fullName: "Short Message Entities"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sme/"
summary: "Entita, která může vytvořit nebo přijmout zprávu služby krátkých zpráv (SMS). Může jít o mobilní stanici, servisní centrum (SMSC) nebo externí aplikaci připojenou k síti. SME jsou koncovými body v arc"
---

SME je mobilní stanice, servisní centrum nebo externí aplikace, která vytváří nebo přijímá zprávu SMS, a v architektuře SMS vystupuje jako koncový bod.

## Popis

Short Message Entity (SME) je základní komponentou architektury služby krátkých zpráv ([SMS](/mobilnisite/slovnik/sms/)) definované 3GPP. Nejde o konkrétní síťový uzel, ale o logickou roli nebo funkci, která může odesílat (vytvářet) a/nebo přijímat (ukončovat) SMS zprávy. Existují tři hlavní typy SME. Za prvé, mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo uživatelské zařízení (UE) je nejběžnějším SME a umožňuje koncovým uživatelům odesílat a přijímat zprávy typu osoba-osoba. Za druhé, Short Message Service Center ([SMSC](/mobilnisite/slovnik/smsc/) nebo [MSC](/mobilnisite/slovnik/msc/)) je klíčové síťové SME zodpovědné za ukládání, přeposílání a směrování zpráv; vytváří zprávy jménem služeb a přijímá zprávy pro doručení mobilním stanicím. Za třetí, externí aplikační platformy (jako e-mailové brány, webové servery nebo podnikové systémy) mohou fungovat jako SME, pokud jsou připojeny k SMSC přes externí rozhraní, což umožňuje zasílání zpráv aplikace-osoba ([A2P](/mobilnisite/slovnik/a2p/)) a stroj-osoba (M2P).

Proces doručování SMS ilustruje interakci SME. Když uživatel odešle zprávu ze své MS (SME-Originator), je zpráva přenesena přes rádiovou síť do Mobile Switching Center (MSC) nebo v pozdějších architekturách do [IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/). MSC zprávu přepošle do SMSC (SME-Recipient pro odeslání). SMSC poté vystupuje jako nový původce, dotazuje se Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) na směrovací informace a přeposílá zprávu do MSC nebo [SGSN](/mobilnisite/slovnik/sgsn/)/MME obsluhující cílovou MS (SME-Recipient pro doručení). Protokol používaný pro komunikaci mezi SMSC a jádrem sítě je typicky MAP (Mobile Application Part) pro GSM/UMTS nebo Diameter pro LTE/5G. Pro externí aplikace jsou běžné protokoly jako SMPP (Short Message Peer-to-Peer) nebo HTTP/API rozhraní.

Role SME je ústřední pro celý ekosystém SMS. Definují koncové body služby. Úkolem sítě je spolehlivě přenést datové jednotky protokolu zpráv (TPDU) mezi těmito entitami. Architektura zajišťuje, že SME nemusí být přímo propojena nebo současně online se svou protistranou SME; schopnost SMSC ukládat a přeposílat zajišťuje asynchronní komunikaci. V moderních sítích se tento koncept rozšiřuje na služby rich communication services (RCS) a zasílání zpráv přes IP, ale základní role SME přetrvává pro tradiční službu SMS, která zůstává klíčovým kanálem pro ověřování (OTP), upozornění a komunikaci typu osoba-osoba, zejména jako záložní služba.

## K čemu slouží

Koncept Short Message Entity byl definován, aby vytvořil jasný, abstraktní model pro architekturu SMS, který odděluje role vytváření/přijímání zpráv od transportních a směrovacích funkcí sítě. Před standardizací bylo třeba specifikovat, co kromě mobilního terminálu může generovat nebo přijímat SMS zprávy. To bylo klíčové pro umožnění přidaných služeb, jako jsou zpravodajská upozornění, bankovní notifikace a brány e-mail na SMS. Model SME formálně uznal, že SMSC samo je jak příjemcem (pro zprávy mu odeslané), tak původcem (pro zprávy, které doručuje), a že externí výpočetní systémy mohou být integrovány jako plnohodnotní účastníci ekosystému zasílání zpráv.

Historicky začala SMS jako služba osoba-osoba, ale její užitečnost se rychle rozšířila. Formální definice SME ve standardech jako TS 23.040 poskytla rámec pro tuto expanzi. Vyřešila problém, jak konzistentně směrovat zprávy do a z nemobilních koncových bodů. Tím, že se se SMSC a externími aplikacemi zacházelo jako s SME s konkrétními adresami (typicky MSISDN nebo služebním kódem), mohla síť uplatňovat jednotné postupy pro odesílání, doručování a řešení chyb. Tato abstrakce byla klíčová pro explozivní růst A2P zpráv, který proměnil SMS v obousměrnou služební platformu. Setrvání konceptu SME ve všech vydáních 3GPP, od R99 až po 5G, podtrhuje jeho účinnost jako základního modelu pro všudypřítomnou službu zasílání zpráv.

## Klíčové vlastnosti

- Logická role zahrnující původce a příjemce zpráv
- Zahrnuje mobilní stanice (UE), servisní centra (SMSC) a externí aplikace
- Definuje koncové body pro vrstvu transportního protokolu (TP) SMS
- Umožňuje asynchronní zasílání zpráv typu store-and-forward prostřednictvím SMSC
- Podporuje adresování pomocí MSISDN, služebních kódů nebo alfanumerických identifikátorů
- Základ pro služby zasílání zpráv typu osoba-osoba i aplikace-osoba

## Související pojmy

- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements

---

📖 **Anglický originál a plná specifikace:** [SME na 3GPP Explorer](https://3gpp-explorer.com/glossary/sme/)
