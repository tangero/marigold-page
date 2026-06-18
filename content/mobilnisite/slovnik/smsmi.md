---
slug: "smsmi"
url: "/mobilnisite/slovnik/smsmi/"
type: "slovnik"
title: "SMSMI – SMS without MSISDN in IMS"
date: 2025-01-01
abbr: "SMSMI"
fullName: "SMS without MSISDN in IMS"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/smsmi/"
summary: "SMSMI je funkce 3GPP, která umožňuje doručování služby krátkých textových zpráv (SMS) přes IP multimediální podsystém (IMS) k uživatelskému zařízení (UE), kterému není přiřazeno telefonní číslo MSISDN"
---

SMSMI je funkce 3GPP umožňující doručování SMS přes IMS k uživatelskému zařízení bez přiřazeného MSISDN s využitím alternativních identifikátorů, jako je externí identifikátor pro zařízení IoT a MTC.

## Popis

[SMS](/mobilnisite/slovnik/sms/) bez [MSISDN](/mobilnisite/slovnik/msisdn/) v IMS (SMSMI) je schopnost definovaná ve specifikaci 3GPP TS 29.338, která umožňuje doručování SMS prostřednictvím IMS k zařízením, která nejsou spojena s klasickým telefonním číslem (MSISDN). V tradiční SMS je MSISDN primárním klíčem pro směrování a identifikaci účastníka. Pro mnoho zařízení IoT/M2M, jako jsou senzory, měřiče nebo vozidlové moduly, je však přidělení MSISDN na zařízení z hlediska číslovacích zdrojů neefektivní a pro jejich komunikační vzorce často zbytečné. SMSMI tento problém řeší využitím identit IMS a profilů předplatného, které jsou oddělené od MSISDN.

Z architektonického hlediska se SMSMI účastní několik entit IMS: IP brána pro krátké zprávy ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)), řídicí funkce sezení pro obsluhu volání ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), domácí registrační server ([HSS](/mobilnisite/slovnik/hss/)) a uživatelské zařízení (UE). Klíčovou inovací je použití alternativního identifikátoru pro směrování SMS. Tím může být veřejná uživatelská identita IMS (např. [SIP](/mobilnisite/slovnik/sip/) [URI](/mobilnisite/slovnik/uri/), jako sip:device123@operator.com) nebo externí identifikátor (definovaný pro [MTC](/mobilnisite/slovnik/mtc/)). HSS ukládá profil účastníka pro zařízení, propojuje tento alternativní identifikátor s předplatným IMS a indikuje, že účastník má povoleno SMSMI. Při doručování SMS na takové zařízení je adresátem tento alternativní identifikátor.

Ústřední roli hraje IP-SM-GW. Ta přijímá odeslanou SMS, typicky zapouzdřenou v požadavku SIP MESSAGE. IP-SM-GW dotazuje HSS (přes rozhraní Sh nebo Cx), aby získala služební profil SMSMI účastníka a potřebné směrovací informace. Protože MSISDN není k dispozici, může HSS poskytnout IMSI nebo indikátor předplatného bez MSISDN. IP-SM-GW následně provede funkci propojení, aby zajistila správné doručení. Může být nutné přeložit cílovou adresu a vyvolat příslušnou služební logiku IMS v S-CSCF. S-CSCF aplikuje počáteční filtrační kritéria (iFC) pro případné směrování SIP MESSAGE na správný aplikační server a nakonec na uživatelské zařízení, pokud je registrované v IMS.

Na straně uživatelského zařízení musí zařízení podporovat IMS a být nakonfigurováno se svou veřejnou uživatelskou identitou IMS. S touto identitou se registruje v IMS síti. Když dorazí SMS jako SIP MESSAGE, IMS klient v zařízení ji zpracuje jako běžnou zprávu SIP. Obsah těla SIP MESSAGE nese datovou část SMS TP (přenosového protokolu). To umožňuje zařízení odesílat a přijímat SMS pomocí své identity IMS, čímž se zcela obejde potřeba MSISDN v signalizační cestě. Tento model se bezproblémově integruje s komunikací založenou na IMS a umožňuje služby SMS pro novou třídu zařízení v rámci celo-IP síťové architektury.

## K čemu slouží

SMSMI bylo vytvořeno za účelem rozšíření služeb SMS na zařízení v prostředí IMS, kterým chybí tradiční MSISDN, což je běžný scénář v internetu věcí (IoT) a komunikaci typu stroj-stroj (MTC). Primární problém, který řeší, je neefektivní využití a vyčerpání číslovacích zdrojů MSISDN. Přidělení jedinečného, směrovatelného telefonního čísla každému senzoru, chytrému měřiči nebo telematickému modulu není škálovatelné a často je regulováno. SMSMI umožňuje těmto zařízením používat SMS – spolehlivý, široce podporovaný a nízkonákladový komunikační protokol – bez spotřeby vzácných čísel E.164.

Historicky byla SMS pevně svázána s MSISDN jako adresou účastníka. Jak se sítě vyvíjely směrem k IMS a operátoři začali nasazovat služby MTC ve velkém měřítku, stalo se toto propojení omezením. Raná řešení MTC někdy používala MSISDN, ale to bylo považováno za nehospodárné provizorium. Motivací pro SMSMI bylo plně využít správu identit v IMS, která je založena na URI a není omezena na čísla E.164. To umožňuje operátorům přiřazovat IoT zařízením flexibilnější identifikátory (jako SIP URI nebo externí ID), což zjednodušuje provizionování a správu.

Dále SMSMI řeší provozní potřebu podpory starších SMS aplikací a služeb pro nová IoT zařízení. Mnoho aplikací M2M spoléhá na SMS pro řídicí příkazy, hlášení dat nebo aktualizace firmwaru díky její jednoduchosti a univerzální podpoře. Tím, že umožňuje SMS přes IMS bez MSISDN, mohou operátoři nabízet tyto stávající řešení M2M na moderních celo-IP sítích bez nutnosti přepracování aplikační vrstvy. Také usnadňuje konvergenci, umožňující jedinému jádru IMS obsluhovat jak tradiční lidské účastníky (s MSISDN), tak strojové účastníky (s alternativními identifikátory) pro služby zasílání zpráv, čímž se snižuje provozní složitost a náklady.

## Klíčové vlastnosti

- Umožňuje doručování SMS přes IMS k účastníkům bez přiřazeného MSISDN s využitím alternativních identifikátorů, jako je SIP URI nebo externí identifikátor
- Využívá IP-SM-GW k provedení překladu adres a propojení mezi protokoly SMS a zasíláním zpráv SIP v IMS
- Spoléhá na profily v HSS, které indikují předplatitelská data SMSMI a mapují alternativní identitu na parametry předplatného IMS
- Podporuje procedury pro SMS iniciované mobilním zařízením i doručované mobilnímu zařízení pro zařízení bez MSISDN v rámci IMS
- Integruje se s řízením služeb IMS prostřednictvím počátečních filtračních kritérií (iFC) v S-CSCF pro případnou interakci s aplikačním serverem
- Usnadňuje nasazení komunikace typu stroj-stroj (MTC) a IoT tím, že šetří číslovací zdroje E.164

## Související pojmy

- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS

---

📖 **Anglický originál a plná specifikace:** [SMSMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/smsmi/)
