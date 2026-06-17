---
slug: "fa-iwf"
url: "/mobilnisite/slovnik/fa-iwf/"
type: "slovnik"
title: "FA/IWF – Fax Adaptor / Interworking Function"
date: 2025-01-01
abbr: "FA/IWF"
fullName: "Fax Adaptor / Interworking Function"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fa-iwf/"
summary: "FA/IWF je funkce faxového adaptéru umístěná v síťové funkci pro propojování sítí (Interworking Function). Umožňuje faxovou komunikaci přes paketové sítě 3GPP tím, že přizpůsobuje tradiční faxové proto"
---

FA/IWF je funkce faxového adaptéru umístěná v síťové funkci pro propojování sítí (Interworking Function), která přizpůsobuje tradiční faxové protokoly pro přenos přes IP v paketových sítích 3GPP, což umožňuje spolupráci se staršími faxovými přístroji nebo sítěmi.

## Popis

Faxový adaptér ve funkci pro propojování sítí ([FA](/mobilnisite/slovnik/fa/)/[IWF](/mobilnisite/slovnik/iwf/)) je kritický síťový prvek definovaný ve specifikacích 3GPP pro zajištění služeb faxu skupiny 3 přes mobilní paketové sítě, jako jsou sítě založené na [GPRS](/mobilnisite/slovnik/gprs/), [EDGE](/mobilnisite/slovnik/edge/) nebo později UMTS/[HSPA](/mobilnisite/slovnik/hspa/). Jeho primární rolí je fungovat jako brána nebo adaptér, který zprostředkovává komunikaci mezi standardní analogovou faxovou signalizací a modulací používanou tradičními faxovými terminály (nebo sítěmi s přepojováním okruhů) a paketovými protokoly používanými v páteřní síti 3GPP. IWF je typicky funkční entita, která může být integrována v rámci uzlu Gateway GPRS Support Node (GGSN) nebo specializované mediální brány.

Z architektonického hlediska se FA/IWF nachází na hranici mezi paketovou doménou (např. IP síť) a externí sítí, kterou může být PSTN/[ISDN](/mobilnisite/slovnik/isdn/) nebo jiná síť s přepojováním okruhů. Když je navázáno faxové spojení z mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) ke staršímu faxovému přístroji, data procházejí přes FA/IWF. Tento prvek provádí převod signálů faxového modemu v reálném čase. To zahrnuje demodulaci analogového faxového signálu z okruhové strany, extrakci obrazových faxových dat, paketizaci těchto dat pomocí protokolů jako TCP/IP nebo UDP/IP a jejich přenos přes paketovou síť k vlastnímu faxovému adaptéru mobilní stanice ([FA/MT](/mobilnisite/slovnik/fa-mt/)). Opačný proces probíhá při odesílání faxů z mobilní stanice.

Fungování je založeno na faxovém přenosovém protokolu T.38 nebo podobných mechanismech pro fax v reálném čase přes IP. FA/IWF implementuje protokolový stack T.38 a zvládá funkce jako spoofing pro kompenzaci zpoždění a kolísání doby přenosu (jitteru) v paketové síti, které jsou škodlivé pro tradiční faxový handshake. Spravuje signalizaci pro řízení hovoru, často rozhraní s protokoly SIP nebo H.323 v IP doméně a ISUP/PRI na okruhové straně. Mezi klíčové komponenty patří funkce pro propojení modemů, engine pro paketizaci/depaketizaci a správa vyrovnávací paměti pro jitter. Jeho úlohou je zajistit transparentní faxovou službu, díky čemuž se paketová síť jeví jako spolehlivé spojení s přepojováním okruhů jak pro faxový terminál, tak pro mobilního uživatele, a tím podporuje životně důležitou starší obchodní službu v moderních sítích.

## K čemu slouží

FA/IWF byl vytvořen k řešení problému podpory starších faxových služeb skupiny 3 v nově vznikajících paketových mobilních sítích. Jak se sítě 3GPP vyvíjely od přepojování okruhů pro hlas (CSD) k efektivnějším paketovým datům (GPRS, UMTS), byl potřebný mechanismus pro přenos faxového provozu v reálném čase, který je citlivý na zpoždění a kolísání doby přenosu (jitter), přes tyto best-effort IP sítě. Bez adaptéru by faxová komunikace selhávala nebo by měla špatnou kvalitu.

Historický kontext představuje přechodové období na počátku 2000. let (přibližně 3GPP Release 4), kdy mobilní operátoři potřebovali zachovat podporu pro obchodně kritické faxové služby během migrace svých páteřních sítí na plně IP architektury. Předchozí přístupy spoléhaly na Circuit Switched Data (CSD) pro fax, které na dobu trvání hovoru vyhradily celý přenosový kanál, což bylo ve srovnání s paketovým přenosem neefektivní využití spektra a síťových zdrojů.

FA/IWF společně s FA/MT tento problém vyřešil definováním standardizovaného řešení pro propojení sítí. Umožnil opětovné využití stávajících faxových přístrojů a služeb, čímž chránil investice operátorů a zajišťoval kontinuitu podnikání. Jeho vytvoření bylo motivováno komerční nutností nabízet kompletní sadu telefonních služeb, včetně faxu, přes nové vysokorychlostní paketové datové sítě, čímž se tyto sítě staly životaschopnou náhradou za všechny tradiční služby s přepojováním okruhů.

## Klíčové vlastnosti

- Zprostředkovává spolupráci mezi analogovou/PCM faxovou signalizací a paketovými protokoly (např. T.38)
- Typicky integrován v rámci síťového uzlu IWF nebo Media Gateway
- Podporuje demodulaci a remodulaci faxu v reálném čase pro přenos přes IP
- Implementuje faxový přenosový protokol T.38 s technikami kompenzace jitteru a spoofingu
- Zajišťuje propojení signalizace pro řízení hovoru (např. ISUP na SIP) pro navázání faxové relace
- Umožňuje transparentní faxovou službu pro mobilní uživatele připojující se k faxovým terminálům v PSTN

## Související pojmy

- [FA/MT – Fax Adaptor / Mobile Terminal](/mobilnisite/slovnik/fa-mt/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 23.045** (Rel-4) — GSM Group 3 Facsimile Service Procedures
- **TS 43.045** (Rel-19) — Group 3 Fax Service in A/Gb Mode PLMN

---

📖 **Anglický originál a plná specifikace:** [FA/IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/fa-iwf/)
