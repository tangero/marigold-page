---
slug: "cksrvcc"
url: "/mobilnisite/slovnik/cksrvcc/"
type: "slovnik"
title: "CKSRVCC – Cipher Key for Single Radio Voice Continuity"
date: 2026-01-01
abbr: "CKSRVCC"
fullName: "Cipher Key for Single Radio Voice Continuity"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cksrvcc/"
summary: "Bezpečnostní klíč používaný k ochraně hlasových hovorů během předání Single Radio Voice Call Continuity (SRVCC) ze sítí LTE/5G do starších sítí 2G/3G. Zajišťuje, že důvěrnost a integrita hovoru jsou z"
---

CKSRVCC je šifrovací klíč používaný k ochraně důvěrnosti a integrity hlasového hovoru během předání SRVCC ze sítí LTE nebo 5G do starších sítí 2G nebo 3G.

## Popis

Cipher Key for Single Radio Voice Continuity (CKSRVCC) je klíčový bezpečnostní parametr definovaný v rámci frameworku 3GPP Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Jeho hlavní funkcí je sloužit jako šifrovací klíč pro zabezpečení hlasového provozu, když je User Equipment (UE) provádějící hovor Voice over LTE (VoLTE) nebo Voice over NR (VoNR) předán do staršího okruhově spínaného (Circuit-Switched, [CS](/mobilnisite/slovnik/cs/)) domény, jako je 2G ([GERAN](/mobilnisite/slovnik/geran/)) nebo 3G (UTRAN), prostřednictvím procedury SRVCC. Toto předání je nezbytné ve scénářích pokrytí, kde končí pokrytí paketově spínané (Packet-Switched, PS) sítě LTE/5G, ale přetrvává pokrytí starší CS hlasové sítě. Bez CKSRVCC by mohlo dojít k narušení zabezpečení, kdy by hovor mohl pokračovat bez šifrování nebo by přešel na slabší starší kryptografické algoritmy.

Generování CKSRVCC je pevně integrováno do bezpečnostní architektury jádra sítě, konkrétně Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) a Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). Když se UE s podporou SRVCC připojí k síti, může HSS/UDM v rámci autentizační procedury odvodit a uložit CKSRVCC spolu s dalšími klíči, jako je K_[ASME](/mobilnisite/slovnik/asme/). CKSRVCC je odvozen z dlouhodobého tajného klíče (K) a dalších parametrů, což zajišťuje jeho kryptografickou oddělenost od klíčů používaných pro zabezpečení PS domény. Během blížícího se předání SRVCC zdrojový MME/AMF načte CKSRVCC (a jeho přidružený integritní klíč IKSRVCC) z HSS/UDM, pokud jej již nemá lokálně uložený, a bezpečně jej přepošle do cílového Mobile Switching Center (MSC) serveru přes rozhraní Sv.

Po přijetí cílový MSC server použije CKSRVCC k odvození skutečného šifrovacího klíče (Kc) používaného starší CS rádiovou přístupovou sítí (např. pomocí algoritmů GSM A5 nebo UMTS f8). Toto odvození je standardizováno, aby byla zajištěna interoperabilita mezi 5G Core (5GC)/EPC a CS doménou. UE provede stejné odvození lokálně. Tento proces zajišťuje, že hlasový hovor přejde z ochrany algoritmy jako AES v PS doméně k ochraně v CS doméně bez potřeby nové autentizační procedury, která by způsobila nepřijatelné přerušení hovoru. CKSRVCC tedy umožňuje plynulou a bezpečnou kontinuitu služby při zachování důvěrnosti uživatelských hlasových dat napříč technologickou hranicí.

Specifikace CKSRVCC v 3GPP TS 33.501 definuje formalizovanou hierarchii klíčů a funkce pro odvozování klíčů. Je součástí sady klíčů specifických pro SRVCC, která zahrnuje také IKSRVCC pro integritu a klíče pro ochranu přidružené signalizace. Jeho zavedení bylo klíčové pro umožnění bezpečných nasazení VoLTE/VoNR, neboť zaplnilo kritickou bezpečnostní mezeru existující v raných implementacích SRVCC, které se někdy během fáze CS fallback spoléhaly na nulové šifrování nebo slabší předem sdílené klíče, což činilo hovory zranitelnými vůči odposlechu.

## K čemu slouží

CKSRVCC byl vytvořen k řešení konkrétního bezpečnostního problému udržení důvěrnosti hovoru během předání mezi různými rádiovými technologiemi (inter-RAT) z bezpečné, paketově spínané sítě 4G/5G do starší okruhově spínané sítě 2G/3G. Před jeho standardizací představovala předání SRVCC významnou zranitelnost. Sítě LTE/5G používají silné šifrování založené na EPS-AKA nebo 5G-AKA (např. 128-EEA1, AES), zatímco starší sítě GSM a UMTS často používaly starší, slabší šifrovací algoritmy (jako A5/1) nebo mohly dokonce fungovat v nešifrovaném režimu. Bez mechanismu pro přenos silného, pro relaci specifického klíče by předání mohlo vést ke snížení úrovně zabezpečení, přerušení šifrování nebo vynucení opětovné autentizace, která by přerušila aktivní hovor.

Historický kontext spočívá ve fázovaném nasazování VoLTE a později VoNR. Operátoři potřebovali způsob, jak poskytovat plynulou hlasovou službu napříč svými smíšenými sítěmi, zejména v oblastech, kde bylo pokrytí LTE/NR dat přerušované, ale pokrytí GSM/UMTS hlasem bylo všudypřítomné. Samotná procedura SRVCC byla definována pro zvládnutí mobility, ale její počáteční specifikace postrádaly robustní, standardizované bezpečnostní řešení pro přenos klíče. CKSRVCC tuto mezeru zaplnil definicí vyhrazeného klíče v rámci hierarchie klíčů AKA, který je odvozen ze silného kořenového klíče a může být namapován na klíčový materiál starší CS domény.

Tím byly odstraněny limity ad-hoc nebo nestandardních implementací a zajištěna konzistentní, vysoká úroveň bezpečnostní záruky pro hlasové hovory bez ohledu na podkladovou přístupovou technologii. Chrání před útoky odposlechu během kritického okna předání i následně v CS doméně, čímž naplňuje celkové bezpečnostní sliby hlasových služeb založených na IMS a splňuje regulatorní a uživatelská očekávání pro soukromou komunikaci. Jeho vytvoření bylo motivováno potřebou učinit z SRVCC skutečně provozovatelsky vhodnou a bezpečnou funkci, což bylo zásadní pro operátory, aby mohli s důvěrou nasazovat VoLTE/VoNR jako primární hlasovou službu.

## Klíčové vlastnosti

- Umožňuje bezpečný přenos šifrovacího kontextu z PS do CS domény během SRVCC
- Odvozen z dlouhodobého klíče účastníka (K) prostřednictvím frameworku AKA, což zajišťuje kryptografickou sílu
- Zabraňuje snížení úrovně zabezpečení a udržuje důvěrnost hovoru při předání z LTE/5G do 2G/3G
- Standardizovaná funkce pro odvozování klíčů pro generování staršího CS šifrovacího klíče (Kc) z CKSRVCC
- Spravován a distribuován prvky jádra sítě HSS/UDM a MME/AMF
- Odstraňuje potřebu opětovné autentizace během předání, čímž zajišťuje plynulou kontinuitu hlasové služby

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [CKSRVCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cksrvcc/)
