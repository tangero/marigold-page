---
slug: "udh"
url: "/mobilnisite/slovnik/udh/"
type: "slovnik"
title: "UDH – User Data Header"
date: 2025-01-01
abbr: "UDH"
fullName: "User Data Header"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/udh/"
summary: "Hlavičková struktura uvnitř SMS (Short Message Service) zprávy, která nese řídicí informace a umožňuje rozšířené funkce zasílání zpráv. Předchází vlastní textovou část a umožňuje spojování zpráv, adre"
---

UDH je hlavička uvnitř SMS zprávy, která nese řídicí informace pro umožnění rozšířených funkcí, jako je spojování zpráv a adresování portů, čímž rozšiřuje základní protokol za pouhý prostý text.

## Popis

User Data Header (UDH) je definované pole v rámci prvku TP-User-Data (TP-UD) krátké zprávy ([SM](/mobilnisite/slovnik/sm/)) v protokolovém zásobníku [SMS](/mobilnisite/slovnik/sms/) dle GSM/3GPP. Jeho primárním účelem je přenášet dodatečné řídicí informace spolu s textovou zprávou uživatele, což umožňuje řadu rozšířených služeb zasílání zpráv. Z architektonického hlediska se nachází na aplikační vrstvě, ale je přenášen transparentně podpůrnými signalizačními vrstvami mobilní sítě (např. [MAP](/mobilnisite/slovnik/map/) přes [SS7](/mobilnisite/slovnik/ss7/)). UDH je umístěn na začátku pole TP-UD a jeho přítomnost je indikována nastavením bitu TP-UDHI (User Data Header Indicator) v SMS Submit nebo Deliver [PDU](/mobilnisite/slovnik/pdu/).

Struktura UDH je založena na informačních prvcích (Information Elements, IEs). Každý [IE](/mobilnisite/slovnik/ie/) má jedno-bajtový identifikátor ([IEI](/mobilnisite/slovnik/iei/)), jedno-bajtové pole délky a samotná data. Tento modulární design umožňuje, aby bylo v rámci jednoho UDH zřetězeno více IE. Mezi klíčové informační prvky UDH patří IE pro spojené krátké zprávy (který umožňuje rozdělení dlouhé zprávy do více SMS segmentů), IE pro adresování aplikačního portu (který umožňuje směrování SMS ke konkrétní aplikaci na zařízení, jako je [WAP](/mobilnisite/slovnik/wap/) push nebo e-mailoví klienti) a IE pro národní jazykový jednorázový posun a uzamčený posun (pro podporu rozšířených znakových sad nad rámec výchozí 7-bitové abecedy GSM).

Princip fungování: Když zařízení chce odeslat rozšířenou SMS (např. dlouhou zprávu nebo binární zprávu pro aplikaci), vytvoří UDH s potřebnými IEs a připojí jej před uživatelská data. Celková délka UDH snižuje prostor dostupný pro vlastní textovou část v daném segmentu. U spojených zpráv obsahuje každý segment UDH se stejným referenčním číslem zprávy, celkovým počtem segmentů a pořadovým číslem segmentu. SMS zásobník přijímacího zařízení použije informace z UDH k opětovnému složení segmentů ve správném pořadí, než je kompletní zpráva předána uživateli nebo cílové aplikaci.

UDH hraje klíčovou roli při umožnění fungování ekosystému SMS. Pro síťové operátory umožňuje poskytovat služby s přidanou hodnotou bez změny základního transportního mechanismu. Pro výrobce zařízení a vývojáře aplikací poskytuje standardizovaný způsob implementace funkcí, jako je zasílání obrázků (přes EMS, které využívá UDH), stahování vyzvánění a Over-The-Air (OTA) provisioning. Zpracování UDH je povinné pro zařízení vyhovující standardu SMS, což zajišťuje interoperabilitu. Specifikace upravující UDH, jako jsou 3GPP TS 23.040 (SMS) a TS 23.048 (Security mechanisms for SMS), podrobně popisují přesné kódování a postupy.

## K čemu slouží

UDH byl vytvořen, aby překonal závažná omezení původního návrhu SMS, který byl koncipován jako jednoduchá služba zasílání textových zpráv o 160 znacích bez vnitřní podpory pro delší zprávy, binární data nebo adresování aplikací. Jak popularita SMS explodovala, uživatelé chtěli posílat zprávy delší než 160 znaků a operátoři chtěli nabízet nové služby, jako jsou loga, vyzvánění a informační upozornění. Problém spočíval v tom, že základní SMS PDU nemělo standardizovaný způsob přenosu těchto dodatečných řídicích informací.

Zavedení UDH v Release 5 poskytlo elegantní, zpětně kompatibilní řešení. Vyčleněním části pole uživatelských dat pro hlavičku umožnilo zavádět nové funkce bez narušení stávajících zařízení, která je nepodporovala (ta by UDH jednoduše ignorovala a zobrazila zbývající text, často jako poškozené znaky). To byl klíčový návrhový princip pro postupný vývoj sítě a zařízení. Vyřešilo to problém fragmentace, ke kterému by došlo, pokud by každý výrobce vymyslel proprietární metody pro spojování zpráv nebo směrování aplikací.

Jeho vytvoření bylo přímo motivováno komerční poptávkou po Enhanced Messaging Service (EMS) a později jako základ pro oznámení Multimedia Messaging Service (MMS). UDH umožnilo, aby se SMS stalo nositelem malých binárních objektů a řídicích příkazů, čímž rozšířilo jeho užitečnost daleko za mez textu mezi lidmi. Vyřešilo omezení pevné délky PDU poskytnutím flexibilního, rozšiřitelného kontejneru pro metadata, což nakonec umožnilo SMS zůvat životaschopnou a univerzální servisní platformou po desetiletí, podporující vše od dvoufázového ověřování až po komunikaci mezi stroji.

## Klíčové vlastnosti

- Je indikován bitem TP-User-Data-Header-Indicator (TP-UDHI) v SMS PDU.
- Skládá se z jednoho nebo více informačních prvků (Information Elements, IEs), z nichž každý má Identifikátor, Délku a Data.
- Umožňuje spojování dlouhých zpráv přes více SMS segmentů.
- Poskytuje adresování aplikačních portů pro směrování SMS ke konkrétním softwarovým aplikacím (např. WAP push, MMS oznámení).
- Podporuje uzamčení a posun pro národní jazyky pro rozšířené znakové sady.
- Tvoří základ pro Enhanced Messaging Service (EMS) pro jednoduché obrázky, zvuky a formátování.

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 29.311** (Rel-19) — Service Level Interworking for Messaging

---

📖 **Anglický originál a plná specifikace:** [UDH na 3GPP Explorer](https://3gpp-explorer.com/glossary/udh/)
