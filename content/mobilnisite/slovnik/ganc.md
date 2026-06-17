---
slug: "ganc"
url: "/mobilnisite/slovnik/ganc/"
type: "slovnik"
title: "GANC – Generic Access Network Controller"
date: 2025-01-01
abbr: "GANC"
fullName: "Generic Access Network Controller"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ganc/"
summary: "Generic Access Network Controller (GANC) je prvek základní sítě, který umožňuje mobilním zařízením přístup ke službám 3GPP přes nelicencované rádiové technologie, jako je Wi-Fi. Funguje jako zabezpeče"
---

GANC je prvek základní sítě, který funguje jako zabezpečená brána a umožňuje mobilním zařízením přístup ke službám 3GPP přes nelicencované rádiové technologie, jako je Wi-Fi, prostřednictvím překladu protokolů.

## Popis

Generic Access Network Controller (GANC) je standardizovaný síťový uzel definovaný 3GPP pro architekturu Generic Access Network ([GAN](/mobilnisite/slovnik/gan/)), známou také jako Unlicensed Mobile Access (UMA). Jeho primární funkcí je sloužit jako konvergenční bod, který zabezpečeně propojuje mobilní uživatelské zařízení (UE) přes IP přístupové sítě (jako je širokopásmové Wi-Fi) s tradiční jádrovou sítí 3GPP. GANC se vůči jádrové síti jeví jako standardní radiový síťový řadič (RNC) pro přepojované služby nebo jako Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) pro paketově přepínané služby, čímž abstrahuje podkladovou nelicencovanou rádiovou technologii. Ukončuje zabezpečené rozhraní Up od UE, které nese tunelovanou signalizaci GSM/GPRS a přenos uživatelských dat přes [IPsec](/mobilnisite/slovnik/ipsec/). GANC plní kritické funkce včetně autentizace, šifrování, registrace a správy mobility pro UE v režimu GAN. Spravuje předávání probíhajících hlasových hovorů a datových relací mezi licencovanou buněčnou sítí (např. [GERAN](/mobilnisite/slovnik/geran/)/UTRAN) a nelicencovanou sítí Wi-Fi, čímž zajišťuje kontinuitu služeb. Architektonicky se GANC skládá z bezpečnostní brány (SEGW) pro vytváření zabezpečených tunelů a jádra GANC, které zajišťuje převod protokolů a správu relací. To operátorům umožňuje rozšířit jejich buněčné hlasové a datové služby do vnitřních a rezidenčních prostředí pomocí nákladově efektivních a široce dostupných širokopásmových připojení, čímž je Wi-Fi efektivně využívána jako další rádiová přístupová technologie pod kontrolou sítě.

## K čemu slouží

GANC byl vytvořen, aby řešil výzvu poskytování bezproblémového pokrytí buněčnými službami uvnitř budov a v oblastech se slabým signálem makro sítě, a to využitím všudypřítomnosti Wi-Fi a širokopásmového internetu. Před [GAN](/mobilnisite/slovnik/gan/) vyžadovaly dvoupásmové telefony Wi-Fi/buňka samostatné, neintegrované klienty pro volání přes Wi-Fi (jako VoIP aplikace), které nenabízely plynulé předání, konzistentní uživatelský zážitek ani integraci se základními buněčnými službami, jako jsou SMS a hlasová schránka. Tato technologie byla klíčovým prvkem pro ranou konvergenci pevné a mobilní sítě ([FMC](/mobilnisite/slovnik/fmc/)), což mobilním operátorům umožnilo konkurovat službám pevné telefonie a snížit míru odchodů zákazníků zlepšením pokrytí v domácnostech. Vyřešila problém 'děr v pokrytí' bez vysokých nákladů na nasazení dalších buněčných makro stanic nebo femtobuněk tím, že využívala vlastní širokopásmové připojení zákazníka jako důvěryhodnou přístupovou větev zpět k operátorskému jádru. Standardizace v 3GPP Rel-8 poskytla framework pro vzájemnou spolupráci dodavatelů pro zabezpečené, operátorské přenesení zátěže na Wi-Fi a volání přes Wi-Fi, což položilo důležité základy pro později vyvinutá řešení, jako je Voice over Wi-Fi (VoWiFi) založené na IP Multimedia Subsystem (IMS) a Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)).

## Klíčové vlastnosti

- Ukončení zabezpečeného IPsec tunelu pro připojení UE přes nedůvěryhodné přístupové sítě
- Převod protokolů mezi signalizací 3GPP (např. RANAP, BSSAP) a IP transportem
- Plynulé předání (HO) hlasových hovorů a datových relací mezi buněčnou a Wi-Fi sítí
- Integrace s prvky jádrové sítě (MSC, SGSN) jako standardní proxy RNC nebo SGSN
- Autentizace, registrace a správa mobility UE pro oblast služby GAN
- Podpora přepojovaného hlasu (GSM), paketově přepínaných dat (GPRS) a služeb SMS přes IP

## Související pojmy

- [GAN – Generative Adversarial Network](/mobilnisite/slovnik/gan/)

## Definující specifikace

- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [GANC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ganc/)
