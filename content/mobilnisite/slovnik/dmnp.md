---
slug: "dmnp"
url: "/mobilnisite/slovnik/dmnp/"
type: "slovnik"
title: "DMNP – Delegated Mobile Network Prefix"
date: 2025-01-01
abbr: "DMNP"
fullName: "Delegated Mobile Network Prefix"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dmnp/"
summary: "Prefix sítě delegovaný operátorem mobilní sítě jiné entitě, například vozidlu nebo IoT bráně, což jí umožňuje fungovat jako mobilní směrovač. Umožňuje lokální přidělování IP adres a síťovou mobilitu p"
---

DMNP je prefix mobilní sítě delegovaný operátorem entitě, jako je vozidlo nebo IoT brána, což jí umožňuje fungovat jako mobilní směrovač pro lokální přidělování IP adres a síťovou mobilitu.

## Popis

Delegovaný prefix mobilní sítě (DMNP) je koncept jádra sítě definovaný v rámci architektury 3GPP pro umožnění síťové mobility a správy lokálních IP adres. Funguje v rámci architektury Network-Based Local IP Access (NB-LIPA) a Selected IP Traffic Offload ([SIPTO](/mobilnisite/slovnik/sipto/)). Operátor mobilní sítě deleguje souvislý blok IP adres (prefix) uživatelskému zařízení (UE), které je autorizováno fungovat jako brána pro Local IP Access ([LIPA](/mobilnisite/slovnik/lipa/)) nebo SIPTO. Toto UE, často mobilní směrovač ve vozidle, vlaku nebo na pevné lokalitě, následně tento prefix používá k poskytnutí IP konektivity dalším zařízením připojeným k němu přes lokální síť (např. Wi-Fi, Ethernet).

Architektonická role DMNP je svázána s připojením k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/) connection), které zřídí bránové UE. Síť, konkrétně Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v Evolved Packet Core (EPC) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core (5GC), přiřadí prefix jako součást procedur zřizování nebo modifikace PDN připojení. Toto delegování se řídí politikami z Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Bránové UE přijímá prefix prostřednictvím Protocol Configuration Options ([PCO](/mobilnisite/slovnik/pco/)) v procedurách PDN připojení.

Po delegování je bránové UE zodpovědné za správu adres v rámci tohoto prefixu. Může provádět funkce obdobné DHCP serveru nebo použít IPv6 stateless address autoconfiguration (SLAAC) k přidělení IP adres z delegovaného prefixu zařízením ve své lokální síti. Veškerý provoz z těchto lokálních zařízení se pro jádro mobilní sítě jeví jako pocházející z PDN připojení bránového UE. Jádro sítě vidí jediný IP tok (nebo bearer) pro agregovaný provoz, což zjednodušuje účtování, vynucování politik a správu mobility pro potenciálně velký počet připojených zařízení.

Význam DMNP spočívá v umožnění škálovatelné, síťově řízené lokalizované konektivity. Umožňuje operátorovi rozšířit svou IP doménu na pohyblivé nebo vzdálené platformy bez nutnosti zřizovat individuální SIM karty pro každé připojené zařízení. To podporuje případy použití jako infotainment systémy ve vozidlech, palubní senzory v hromadné dopravě nebo dočasné sítě pro akce, kde brána poskytuje řízenou IP konektivitu jako rozšíření sítě mobilního operátora.

## K čemu slouží

DMNP byl zaveden k řešení výzev škálovatelnosti a správy při připojování četných zařízení v lokalizovaných prostředích, jako jsou vozidla, vlaky nebo dočasné prostory pro akce, k mobilní síti. Před jeho zavedením potřebovalo každé zařízení vyžadující buněčnou konektivitu vlastní předplatné a SIM kartu, což vedlo ke složitému zřizování, vysoké signalizační zátěži jádra sítě při událostech mobility a neefektivnímu využití prostoru IP adres. To bylo zvláště problematické pro scénáře Internetu věcí (IoT) a mobilní hotspoty.

Koncept byl motivován potřebou síťového offloadu a lokalizovaného breakoutu. Řešení jako LIPA a SIPTO cílila na směrování provozu přímo na síťové hraně, ale DMNP poskytl mechanismus pro delegování pravomocí správy adres na hraniční zařízení samotné. To umožňuje mobilnímu operátorovi zachovat kontrolu (prostřednictvím politik delegování), zároveň však zmocňuje bránové UE k efektivní správě své lokální sítě. Řeší problém poskytování bezproblémové IP mobility pro celou podsíť zařízení, když se brána pohybuje, protože jádro sítě potřebuje spravovat pouze mobilitu PDN připojení bránového UE. Historicky to zaplnilo mezeru mezi čistě terminálovým mobilním směrováním a plnohodnotnými síťovými řešeními mobility, nabízejíc vyvážený přístup pro operátorsky řízené mobilní sítě.

## Klíčové vlastnosti

- Umožňuje UE fungovat jako mobilní směrovač pro lokální síť s využitím IP adresního prostoru delegovaného operátorem.
- Podporuje delegování prefixů pro IPv4 i IPv6 v kontextu PDN připojení.
- Integruje se s řízením politik (PCRF/PCF) pro autorizované delegování na základě předplatného a síťových politik.
- Snižuje signalizaci v jádře sítě agregací provozu z více lokálních zařízení na jediné PDN připojení/bearer.
- Umožňuje síťovou mobilitu pro celé podsítě, protože delegovaný prefix se pohybuje spolu s bránovým UE.
- Umožňuje bránovému UE lokální přidělování IP adres (např. přes DHCPv6 nebo SLAAC) bez zapojení jádra sítě pro každé jednotlivé zařízení.

## Související pojmy

- [LIPA – Local IP Access](/mobilnisite/slovnik/lipa/)
- [SIPTO – Selected IP Traffic Offload](/mobilnisite/slovnik/sipto/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)

---

📖 **Anglický originál a plná specifikace:** [DMNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmnp/)
