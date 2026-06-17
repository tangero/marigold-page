---
slug: "connack"
url: "/mobilnisite/slovnik/connack/"
type: "slovnik"
title: "CONNACK – Connect Acknowledgement"
date: 2025-01-01
abbr: "CONNACK"
fullName: "Connect Acknowledgement"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/connack/"
summary: "CONNACK je protokolová zpráva používaná v sítích 3GPP k potvrzení úspěšného navázání připojení. Je to klíčová součást signalizace správy připojení, která potvrzuje, že síť žádost o připojení zpracoval"
---

CONNACK je potvrzovací protokolová zpráva v sítích 3GPP, která potvrzuje úspěšné přijetí žádosti o připojení a umožňuje spolehlivé nastavení relace.

## Popis

CONNACK (Connect Acknowledgement) je základní signalizační zpráva v architektuře protokolů 3GPP, konkrétně v rámci procedur navazování připojení. Funguje jako odpověď na zprávu CONNECT a signalizuje, že síť úspěšně zpracovala pokus o navázání připojení a je připravena pokračovat v relaci. Zprávu generuje síťová strana (typicky entity řídicí roviny jádra sítě) a odesílá ji zpět žadateli, kterým může být uživatelské zařízení (UE) nebo jiný síťový uzel iniciující připojení.

Z architektonického hlediska se CONNACK řadí do vrstvového modelu protokolů systémů 3GPP a nachází se v signalizačních protokolech řídicí roviny. Není vázána na jednu konkrétní protokolovou vrstvu, ale je implementována v různých protokolových zásobnících v závislosti na typu připojení – například ve signalizaci Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) pro připojení k jádru sítě nebo v rámci specifických aplikačních protokolů. Zpráva obsahuje nezbytné informační prvky, které potvrzují přijetí připojení, a může zahrnovat parametry jako identifikátory připojení, vyjednané profily kvality služeb (QoS) a informace o bezpečnostním kontextu nezbytné pro navázanou relaci.

Z funkčního pohledu, když je odeslána zpráva CONNECT (iniciující žádost o připojení), přijímající síťová entita tuto žádost zpracuje provedením řízení přístupu, alokace prostředků a bezpečnostních procedur. Po úspěšném dokončení těchto kontrol entita vygeneruje zprávu CONNACK. Tato zpráva prochází zpět síťovými vrstvami k iniciátorovi, čímž dokončí handshake. CONNACK typicky obsahuje výsledkový kód indikující úspěch nebo, v některých implementacích, konkrétní příčiny selhání, pokud bylo připojení odmítnuto, což umožňuje žadateli pochopit výsledek a případně opakovat pokus s upravenými parametry.

Její role v síti je klíčová pro spolehlivou správu relací. Poskytnutím explicitního potvrzení CONNACK zabraňuje nejednoznačným stavům připojení, kdy by si žadatel nemusel být jistý, zda je připojení aktivní. To je zvláště důležité v mobilním prostředí, kde mohou být rádiové podmínky nestabilní a signalizační zprávy se mohou ztratit. Mechanismus CONNACK v kombinaci s časovači a procedurami pro opakovaný přenos zajišťuje robustní navazování připojení a tvoří základ pro následné datové toky, ať už pro hlasové hovory, datové relace nebo samotné signalizační výměny.

## K čemu slouží

Zpráva CONNACK byla vytvořena, aby řešila základní potřebu spolehlivého a potvrzeného navazování připojení v telekomunikačních sítích. Před standardizovanými potvrzovacími mechanismy mohlo být navazování připojení nejednoznačné – žádost mohla být odeslána, ale bez potvrzení nemohl iniciující subjekt mít jistotu, zda byly prostředky alokovány a relace je připravena. To vedlo k neefektivnímu využití prostředků (např. rezervování prostředků pro potenciálně neúspěšná připojení) a špatné uživatelské zkušenosti, protože aplikace mohly předpokládat, že připojení je aktivní, když nebylo.

Historicky, jak se 3GPP vyvíjelo od GSM přes UMTS (Release 99/4) a dále, rostla složitost služeb a různorodost typů připojení (circuit-switched, packet-switched, IMS). To si vyžádalo robustní, obecný potvrzovací mechanismus, který by mohl být adaptován napříč různými protokolovými zásobníky a servisními doménami. CONNACK poskytuje toto standardizované potvrzení, což umožňuje interoperabilitu mezi síťovými prvky od různých výrobců a zajišťuje konzistentní chování pro správu připojení.

CONNACK dále řeší problémy související s efektivitou sítě a správou poruch. Explicitním potvrzením připojení může síť spustit přesné počáteční body účtování, aplikovat řídicí politiky a vést přesné záznamy o stavu relace. V případech selhání CONNACK (nebo její varianty s negativním potvrzením) poskytuje diagnostické informace, což umožňuje síti a UE provést vhodné procedury obnovy po chybě nebo přechodu na záložní řešení, čímž se zvyšuje celková odolnost systému a dostupnost služeb.

## Klíčové vlastnosti

- Explicitní potvrzení přijetí žádosti o připojení
- Nese parametry specifické pro připojení a vyjednané informace o QoS
- Podporuje indikace výsledku úspěchu i selhání pro robustní zpracování chyb
- Integruje se s různými protokoly řídicí roviny 3GPP (např. NAS, RRC, aplikační vrstva)
- Umožňuje synchronizovaný stav relace mezi UE a síťovými entitami
- Usnadňuje spolehlivé navázání relace jako součást procedury handshake s více zprávami

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 27.001** (Rel-19) — Terminal Adaptation Functions for PLMN

---

📖 **Anglický originál a plná specifikace:** [CONNACK na 3GPP Explorer](https://3gpp-explorer.com/glossary/connack/)
