---
slug: "ema"
url: "/mobilnisite/slovnik/ema/"
type: "slovnik"
title: "EMA – Electronic Message Association"
date: 2005-01-01
abbr: "EMA"
fullName: "Electronic Message Association"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ema/"
summary: "EMA byl raný servisní rámec 3GPP pro multimediální zprávy, který definoval protokoly pro odesílání a přijímání zpráv obsahujících text, obrázky, audio a video. Poskytoval standardizovanou alternativu"
---

EMA je raný servisní rámec 3GPP, který standardizoval protokoly pro odesílání a přijímání multimediálních zpráv za účelem zajištění interoperability mezi různými operátory a koncovými zařízeními.

## Popis

Electronic Message Association (EMA) byla servisní schopnost definovaná v raných vydáních 3GPP, konkrétně v kontextu služby Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)). Poskytovala standardizovaný architektonický rámec a sadu protokolů pro výměnu multimediálních zpráv. Systém založený na EMA zahrnoval několik klíčových funkčních komponent: MMS User Agent (na uživatelském zařízení – User Equipment), MMS Relay/Server (který ukládal a přeposílal zprávy) a přidružené databáze, jako je MMS User Profile. Protokoly definované pro komunikaci mezi těmito entitami zahrnovaly MM1 (mezi UE a Relay/Server), MM3 (mezi Relay/Server a externími servery email/SMTP), MM4 (pro komunikaci mezi MMS Relay různých operátorů) a MM7 (pro rozhraní poskytovatelů přidaných služeb).

Fungování EMA bylo založeno na modelu store-and-forward (uložit a přeposlat). Když uživatel odeslal MMS, User Agent odeslal zprávu (pomocí WAP nebo [HTTP](/mobilnisite/slovnik/http/) POST přes MM1) svému domácímu MMS Relay/Serveru. Tento server pak zprávu zpracoval, což zahrnovalo kontrolu adresy příjemce, aplikaci servisní logiky na základě profilu odesílatele nebo příjemce (např. omezení velikosti zprávy, adaptace obsahu) a určení dalšího kroku. Pokud byl příjemce v jiné síti, server zprávu přeposlal pomocí standardizovaného protokolu MM4 na domácí MMS Relay/Server příjemce. Ten pak upozornil User Agent příjemce (přes MM1) na čekající zprávu, kterou si agent mohl následně stáhnout. Tento proces umožňoval asynchronní doručování a zpracování zpráv, které mohly být velké nebo vyžadovaly, aby bylo zařízení příjemce zapnuté a v dosahu sítě.

Její role v síti byla jako klíčový prostředek pro interoperabilní multimediální zprávy v éře 2.5G a 3G. Před rozšířením internetových messagingových aplikací bylo MMS primární metodou pro posílání fotek a audio klipů mezi mobilními uživateli. EMA poskytovala nezbytný spojovací článek, který umožňoval, aby MMS odeslané účastníkem v síti Operátora A pomocí telefonu Nokia bylo úspěšně doručeno účastníkovi v síti Operátora B používajícímu telefon Sony Ericsson. Definovala formáty obsahu (jako SMIL pro prezentaci), záznamy o účtování (charging data records) a nastavení soukromí, čímž se MMS stalo zpoplatnitelnou, standardizovanou službou nedílnou součástí portfolia služeb operátorů.

## K čemu slouží

EMA byla vytvořena k řešení problému proprietárních, neinteroperabilních systémů multimediálních zpráv na počátku 21. století. Jak se mobilní sítě vyvíjely od hlasu a SMS k podpoře dat ([GPRS](/mobilnisite/slovnik/gprs/), [EDGE](/mobilnisite/slovnik/edge/)), byla zde silná poptávka trhu po posílání obrázků a audia. Bez standardu by však každý výrobce nebo operátor mohl vyvíjet vlastní systém, což by vedlo k fragmentovanému trhu, kde by si uživatelé na různých sítích nebo s různými telefony nemohli vyměňovat zprávy. EMA, jak ji definoval 3GPP, poskytovala tento chybějící standard a umožnila globální interoperabilitu.

Technologie řešila omezení jednoduché SMS, která byla omezena na 160 znaků textu, a proprietárních řešení pro obrázkové zprávy. Definovala kompletní servisní architekturu, která dokázala zpracovat různé typy médií, přizpůsobit obsah schopnostem zařízení, komunikovat s externími emailovými systémy a podporovat flexibilní modely účtování. To umožnilo operátorům nasadit službu generující příjmy s jasnou cestou pro další vývoj. Historický kontext představuje přechod od přepojování okruhů u SMS k multimediálním službám s přepojováním paketů, využívající nové IP schopnosti sítí GPRS a UMTS.

Motivace pro její zařazení do 3GPP pramenila z touhy vytvořit jednotnou vrstvu mobilních multimediálních služeb, která by mohla být přijata globálně, podobně jako úspěch SMS. Standardizací protokolů a rozhraní snížila fragmentaci trhu, snížila náklady pro výrobce koncových zařízení (kteří mohli stavět podle jednoho standardu) a dala operátorům konkurenceschopnou službu proti vznikajícím internetovým alternativám. Položila základy pro pozdější služby rich communication.

## Klíčové vlastnosti

- Standardizovaná architektura typu store-and-forward (uložit a přeposlat) pro multimediální zprávy
- Definovala sadu interoperabilních protokolů (MM1, MM3, MM4, MM7) mezi komponentami systému
- Podporovala obsah zpráv včetně textových, obrazových, audio a video formátů
- Obsahovala funkce adaptace obsahu podle schopností zařízení příjemce
- Specifikovala rozhraní pro účtování a záznamy o účtování (charging data records) pro fakturaci
- Umožňovala propojení mezi MMS systémy různých operátorů

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition

---

📖 **Anglický originál a plná specifikace:** [EMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ema/)
